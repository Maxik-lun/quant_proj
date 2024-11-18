import httpx
import asyncio
import datetime
import pandas as pd
from typing import Iterable, Final, cast, Optional
from dataclasses import dataclass

# Режимы по умолчанию для запросов
DEFAULT_ENGINE: Final = "stock"
DEFAULT_MARKET: Final = "shares"
DEFAULT_BOARD: Final = "TQBR"
# Ключевые плейсхолдеры и константы для запросов
SECURITIES: Final = "securities"
CANDLE_BORDERS: Final = "candleborders"
CANDLES: Final = "candles"

Values = str | int | float
TableRow = dict[str, Values]
Table = list[TableRow]
TablesDict = dict[str, Table]
WebQuery = dict[str, str | int]

# @dataclass(eq=False, repr=True)
# class Candle:
#     ticker: str
#     dtime: datetime.datetime
#     open: float
#     high: float
#     low: float
#     close: float
#     volume: int

class ISSMoexError(Exception):
    """Ошибки во время обработки запросов."""

def make_url(
    *,
    history: bool | None = None,
    engine: str | None = None,
    market: str | None = None,
    board: str | None = None,
    security: str | None = None,
    ending: str | None = None,
) -> str:
    """Формирует URL для запроса."""
    url_parts = ["https://iss.moex.com/iss"]
    if history:
        url_parts.append("/history")
    if engine:
        url_parts.append(f"/engines/{engine}")
    if market:
        url_parts.append(f"/markets/{market}")
    if board:
        url_parts.append(f"/boards/{board}")
    if security:
        url_parts.append(f"/securities/{security}")
    if ending:
        url_parts.append(f"/{ending}")
    url_parts.append(".json")
    return "".join(url_parts)

def make_query(
    *,
    question: str | None = None,
    interval: int | None = None,
    start: str | None = None,
    end: str | None = None,
    table: str | None = None,
    columns: Iterable[str] | None = None,
) -> dict[str, str | int]:
    """Формирует дополнительные параметры запроса к MOEX ISS.

    :param question:
        Строка с частью характеристик бумаги для поиска.
    :param interval:
        Размер свечки.
    :param start:
        Начальная дата котировок.
    :param end:
        Конечная дата котировок.
    :param table:
        Таблица, которую нужно загрузить (для запросов, предполагающих наличие нескольких таблиц).
    :param columns:
        Кортеж столбцов, которые нужно загрузить.

    :return:
        Словарь с дополнительными параметрами запроса.
    """
    query: dict[str, str | int] = {}
    if question:
        query["q"] = question
    if interval:
        query["interval"] = interval
    if start:
        query["from"] = start
    if end:
        query["till"] = end
    if table:
        query["iss.only"] = f"{table},history.cursor"
    if columns:
        query[f"{table}.columns"] = ",".join(columns)
    return query

def _cursor_block_size(start: int, cursor_table: Table) -> int:
    cursor, *wrong_data = cursor_table
    if wrong_data or cast(int, cursor["INDEX"]) != start:
        raise ISSMoexError(f"Некорректные данные history.cursor: {cursor_table}")
    block_size = cast(int, cursor["PAGESIZE"])
    if start + block_size < cast(int, cursor["TOTAL"]):
        return block_size
    return 0

async def get(session: httpx.AsyncClient, url: str, query: WebQuery) -> TablesDict:
        """Загрузка данных.
        :param start:
            Номер элемента с которого нужно загрузить данные. Используется для дозагрузки данных,
            состоящих из нескольких блоков. При отсутствии данные загружаются с начального элемента.

        :return:
            Блок данных с отброшенной вспомогательной информацией - словарь, каждый ключ которого
            соответствует одной из таблиц с данными. Таблицы являются списками словарей, которые напрямую
            конвертируются в pandas.DataFrame.
        :raises ISSMoexError:
            Ошибка при обращении к ISS Moex.
        """
        response = await session.get(url, params=query)
        data = response.raise_for_status().json()
        if isinstance(data, list):
            return data[1]
        else:
            return data

async def _iterator_maker(session: httpx.AsyncClient, url: str, start_query: WebQuery | None = None):
    start = 0
    query = {"iss.json": "extended", "iss.meta": "off"} | start_query
    while True:
        query["start"] = start
        response = await get(session, url, query)
        if (cursor_table := response.get("history.cursor")) is not None:
            response.pop("history.cursor")
            yield response
            block_size = _cursor_block_size(start, cursor_table)
        else:
            yield response
            table_name = next(iter(response))
            block_size = len(response[table_name])
        if not block_size:
            return
        start += block_size

async def get_market_candles(
    session: httpx.AsyncClient,
    security: str,
    interval: int = 24,
    start: str | None = None,
    end: str | None = None,
    market: str = DEFAULT_MARKET,
    engine: str = DEFAULT_ENGINE,
) -> Table:
    """Получить свечи в формате HLOCV указанного инструмента на рынке для основного режима торгов.

    Если торговля идет в нескольких основных режимах, то на один интервал времени может быть выдано
    несколько свечек - по свечке на каждый режим. Предположительно такая ситуация может произойти для
    свечек длиннее 1 дня.

    Описание запроса - https://iss.moex.com/iss/reference/155

    :param session:
        Сессия http соединения.
    :param security:
        Тикер ценной бумаги.
    :param interval:
        Размер свечки - целое число 1 (1 минута), 10 (10 минут), 60 (1 час), 24 (1 день), 7 (1 неделя),
        31 (1 месяц) или 4 (1 квартал). По умолчанию дневные данные.
    :param start:
        Дата вида ГГГГ-ММ-ДД. При отсутствии данные будут загружены с начала истории.
    :param end:
        Дата вида ГГГГ-ММ-ДД. При отсутствии данные будут загружены до конца истории.
    :param market:
        Рынок - по умолчанию акции.
    :param engine:
        Движок - по умолчанию акции.

    :return:
        Список словарей, которые напрямую конвертируется в pandas.DataFrame.
    """
    table_name = CANDLES
    url = make_url(engine=engine, market=market, security=security, ending=table_name)
    query = make_query(interval=interval, start=start, end=end)
    table_dict: TablesDict = {}
    async for block in _iterator_maker(session, url, query):
        for table_name, table_rows in block.items():
            table_dict.setdefault(table_name, []).extend(table_rows)
    # """Извлекает конкретную таблицу из данных."""
    try:
        table = table_dict[table_name]
    except KeyError as err:
        raise ISSMoexError(f"Отсутствует таблица {table_name} в данных")
    return table

async def get_moex_data(start: str, end: str, secids: Optional[Iterable[str]] = None):
    async with httpx.AsyncClient(timeout=httpx.Timeout(timeout=None)) as session:
        async def process_candles(secid):
            ohlc_tmp = await get_market_candles(session, security = secid, start = start, end = end)
            ohlc_tmp = pd.DataFrame(ohlc_tmp)
            ohlc_tmp['secid'] = secid
            return ohlc_tmp
        request_url = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json"
        moex_info_resp = (await session.get(request_url)).raise_for_status().json()
        moex_info_df = pd.DataFrame(moex_info_resp["securities"]['data'], 
                                    columns = moex_info_resp["securities"]['columns'])
        moex_info_df.columns = moex_info_df.columns.str.lower()
        if secids is None:
            secids = moex_info_df['secid']
        tasks = [process_candles(secid) for secid in secids]
        ohlc_data = await asyncio.gather(*tasks)
    moex_candles = pd.concat(ohlc_data, axis = 0)
    return moex_info_df, moex_candles

def download_imoex_contituents(url = "https://fs.moex.com/files/15237", filepath = 'data/imoex_content.xlsx'):
    response = httpx.get(url)
    with open(filepath, "wb") as handle:
        handle.write(response.content)