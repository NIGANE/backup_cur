from typing import Any
from functools import wraps

def greeting_wrapper(fn: callable) -> callable:
    @wraps(fn)
    def wrapper(*ar: Any, **key: Any) -> None:
        """wrapper docs"""
        print("before executing")
        fn(*ar, key) if key else fn(*ar)
        print("after executing")
    return wrapper

@greeting_wrapper
def say_hi(name: str) -> None:
    """greeting docs"""
    print("hi:", name)

help(say_hi)