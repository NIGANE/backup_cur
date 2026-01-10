def ft_count_harvest_iterative():
    count = int(input("Days until harvest: "))
    for day in range(count):
        print(f"Day {day + 1}")
    print("Harvest time!")
