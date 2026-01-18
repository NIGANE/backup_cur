#!/usr/bin/python3
import math


def parsing_cordinates(data: str) -> tuple[int, int, int]:
    storing = []
    try:
        for ele in data.split(','):
            storing.append(int(ele))
        return (storing[0], storing[1], storing[2])
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{data}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


def ft_coordinate_system(data: tuple[int]) -> None:
    x2, y2, z2 = data
    x1, y1, z1 = (0, 0, 0)
    diff = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between (0, 0, 0) and {data}: {diff:.2f}")


def unpacke(data: tuple[int]) -> None:
    print(f"Playser at x={data[0]}, y={data[1]}, z={data[2]}")
    print(f"Coordinates: X={data[0]}, Y={data[1]}, Z={data[2]}")


def main() -> None:
    print("=== Game Coordinate System ===")
    print("")
    data = (10, 20, 5)
    print(f"Position created: {data}")
    ft_coordinate_system(data)
    print("")
    str_to_parse = "3,4,0"
    print(f"Parsing coordinates: \"{str_to_parse}\"")
    tp = parsing_cordinates(str_to_parse)
    print(f"Parsed position: {tp}")
    ft_coordinate_system(tp)
    print("")
    bad_str_parse = "abc,def,ghi"
    tp = parsing_cordinates(bad_str_parse)
    print("")
    print("Unpacking demonstration:")
    p = (3, 4, 0)
    unpacke(p)


if (__name__ == "__main__"):
    main()
