#!/usr/bin/python3
import sys


def valid_integer(s: str) -> bool:
    for c in s:
        if (c not in "0123456789"):
            return False
    return True


def arr_print(data: list[int]):
    i = 0
    count = len(data)
    print("[", end="")
    while (i < count):
        print(f"{data[i]}", end="")
        if (i + 1 != count):
            print(", ", end="")
        i += 1
    print("]")


def ft_score_analytics() -> None:
    args = sys.argv
    data = []
    count = len(sys.argv)
    i = 1
    print("=== Player Score Analytics ===")
    if (count > 1):
        try:
            while (i < count):
                if (not valid_integer(args[i])):
                    raise ValueError(
                        "oops, I typed 'banana' instead of '1000'"
                        )
                data.append(int(args[i]))
                i += 1
        except ValueError as e:
            print(e)
        else:
            print("Scores processed:", end="")
            arr_print(data)
            print(f"Total players: {len(data)}")
            print(f"Total score: {sum(data)}")
            print(f"Average score: {(sum(data) / (len(data) - 1)):.1f}")
            print(f"High score: {max(data)}")
            print(f"Low score: {min(data)}")
            print(f"Score range: {max(data) - min(data)}")
            print("")
    else:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py ",
            "<score1> <score2> ..."
            )


if (__name__ == "__main__"):
    ft_score_analytics()
