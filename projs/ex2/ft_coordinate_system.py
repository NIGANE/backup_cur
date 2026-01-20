#!/usr/bin/python3
import math


def parsing_cordinates(data: str) -> tuple[int]:
    storing = []
    try:
        for ele in data.split(','):
            storing.append(int(ele))
        if ne_len(storing) > 3:
            raise ValueError("too many values to unpack (expected 3)")
        return (storing[0], storing[1], storing[2])
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{data}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


def ne_len(data: tuple) -> int:
    i = 0
    for ele in data:
        i += 1
    return i


def ft_coordinate_system(data: tuple[int]) -> None:
    re = tuple()
    if (isinstance(data, str)):
        data = parsing_cordinates(data)
    if (data is None):
        return
    try:
        i = 0
        if ne_len(data) > 3:
            raise ValueError("too many values to unpack (expected 3)")
        while i < ne_len(data):
            re = (*re, int(data[i]))
            i += 1
    except ValueError as e:
        print(e)
    else:
        x2, y2, z2 = data
        x1, y1, z1 = (0, 0, 0)
        print(f"Position created: {data}")
        diff = float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
        print(f"Distance between (0, 0, 0) and {data}: {diff:.2f}")


def unpacke(data: tuple[int]) -> None:
    if (isinstance(data, str)):
        data = parsing_cordinates(data)
    if (data is None):
        return
    re = tuple()
    try:
        i = 0
        if ne_len(data) > 3:
            raise ValueError("too many values to unpack (expected 3)")
        while i < ne_len(data):
            re = (*re, int(data[i]))
            i += 1
    except ValueError as e:
        print(e)
    else:
        print(f"Playser at x={data[0]}, y={data[1]}, z={data[2]}")
        print(f"Coordinates: X={data[0]}, Y={data[1]}, Z={data[2]}")


def main() -> None:
    print("=== Game Coordinate System ===")
    print("")
    data = (10, 20, 5)
    ft_coordinate_system(data)
    print("")
    str_to_parse = "3,4,0"
    print(f"Parsing coordinates: \"{str_to_parse}\"")
    tp = parsing_cordinates(str_to_parse)
    print(f"Parsed position: {tp}")
    ft_coordinate_system(tp)
    print("")
    bad_str_parse = "abc,def,ghi"
    parsing_cordinates(bad_str_parse)
    print("")
    print("Unpacking demonstration:")
    unpacke(tp)


if (__name__ == "__main__"):
    main()
