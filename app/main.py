from typing import Callable, TypeVar


T = TypeVar("T")


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs) -> list[T]:
        args_key = args + tuple(kwargs.items())
        if args_key in cached_results:
            print("Getting from cache")
            return cached_results[args_key]
        result = func(*args, **kwargs)
        cached_results[args_key] = result
        print("Calculating new result")
        return result
    return wrapper
