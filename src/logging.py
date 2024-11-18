# loggings utils
import asyncio
import functools
from loguru import logger


# wrapper for logging function entry and exit
def log_function_call(*, when_entered=True, when_exited=True, level="DEBUG"):
    def wrapper(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            name = func.__name__
            logger_ = logger.opt(depth=1)
            if when_entered:
                logger_.log(
                    level,
                    "Entering '{}' (args={}, kwargs={})",
                    name,
                    args,
                    kwargs,
                )
            try:
                result = func(*args, **kwargs)
            except Exception as error:
                if when_exited:
                    logger_.log(
                        level,
                        "Exiting '{}' (with exception: {})",
                        name,
                        str(error),
                    )
                raise
            if when_exited:
                logger_.log(level, "Exiting '{}' (result={})", name, result)
            return result
        # some magic for async functions
        if asyncio.iscoroutinefunction(func):
            return functools.update_wrapper(asyncio.coroutine(wrapped), func)
        return functools.update_wrapper(wrapped, func)
    return wrapper