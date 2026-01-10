def ft_harvest_total():
    total = 0
    i = 0
    while i < 3:
        sum = input(f"Day {i+1} harvest: ")
        total = total + int(sum)
        i = i + 1
    print(f"Total harvest: {total}")
