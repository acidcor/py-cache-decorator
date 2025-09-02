from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cashe_dics = {}
    def casher(*args) -> Any:
        if args in cashe_dics:
            print("Getting from cache")
            return cashe_dics[*args]
        else:
            print("Calculating new result")
            result = func(*args)
            cashe_dics[*args] = result
            return result
    return casher