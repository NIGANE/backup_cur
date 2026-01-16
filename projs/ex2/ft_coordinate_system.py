import sys

def parsing_cordinates(data: list[str]):
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

def ft_coordinate_system() -> None:
    args = sys.args
    if (args > 1):
        parsing_cordinates(args[1:])
    else:
            
