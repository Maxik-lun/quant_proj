Постановка задачи

- Необходимо выдвинуть торговую гипотезу, например, будем покупать топ-10 акций из индекса МосБиржи, которые имеют наибольшие дивиденды, взвешивать будем по коэффициенту Шарпа; проверяем, насколько эффективен такой портфель относительно индекса МосБиржи.

- Определить критерии принятия стратегии в прод.

- Выписать торговый юниверс, торговые правила, бенчмарк, другие параметры, которые определяют суть стратегии и исследования.

- Выгрузить и подготовить данные. Провести эджаст цен на дивиденды, сплиты и другие корпоративные события. Провести EDA.

- Провести бэктестирование и кросс-валидацию торговой стратегии с использованием готовых пакетов либо написать необходимые методы самостоятельно, если в пакетах была обнаружена неточность или они просто не подходят под задачу.

- Провести анализ торговой стратегии, проанализировать метрики. Найти плюсы, минусы, преимущества и недостатки решения.

- Проверить критерии принятия стратегии в прод. Достаточно ли перформанса для запуска стратегии или гипотеза невалидная.

- Даже если гипотезу не удалось подтвердить, необходимо разработать модуль, который будет эмулировать торговлю и ребалансировку портфеля в любом формате: вывод ордеров в консоль, отправка в телеграм, отправка сообщений брокеру, как удобнее.

- Пожалуйста, будьте осторожны в торговле на реальные деньги. Не инвестируйте средства, которые не готовы потерять.

- Разработанные методы необходимо сдать в формате юпитер-ноутбука или питон-файла на вкладке Задания. Доступ откроется 5 ноября.

- Дедлайн 12 ноября 12:59:59 по Москве. На проверку возьмем неделю.

Критерии оценки

1. Стратегия разработана end-to-end, подготовлен код для выгрузки и обработки данных, проведен бэктест и кросс-валидация стратегии, подготовлен код симуляции торговли. Код рабочий. Выбран адекватный бенчмарк; проведено качественное и количественное сравнение стратегии; приведены метрики.

2. На «хорошую» оценку: использование правила «ответ — число»; чистый код и чистая архитектура; понятное для «соседа по трейд деску» описание кода. Стратегия оправдана, имеется мотивация торговой гипотезы, например, шортить компании на букву «С» — достаточно странная торговая гипотеза; а вот шортить бумаги, которые выпадают из индекса — имеет место быть. Нам важно, что вы понимаете, что и зачем торгуете. Проведено дополнительное тестирование стратегии: копулы, симуляции, демо-счет, пр.