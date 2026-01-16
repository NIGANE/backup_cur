import sys


def ft_command_quest() -> None:
    args = sys.argv
    count = len(args)
    i = 0
    if (count < 1):
        print("No arguments provided!")
    print(f"Program name: {args[0]}")
    if (count > 1):
        print(f"Arguments received: {count - 1}")
        while (i < count):
            print(f"Argument {i + 1}: {args[i]}")
        print(f"Total arguments: {count}")