from typing import Any

def greeting_wrapper(fn: callable) -> callable:
    def wrapper(*ar: Any, **key: Any) -> None:
        print("before executing")
        print(ar)
        print(key)
        fn(*ar, key) if key else fn(*ar)
        print("after executing")
    return wrapper

# @greeting_wrapper
def say_hi(name: str) -> None:
    print("hi:", name)

say_hi = greeting_wrapper(say_hi)

say_hi("achraf")