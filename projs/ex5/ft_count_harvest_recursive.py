def rep(x):
    if x <= 0:
        return
    rep(x - 1)
    print("Day ", x)


def ft_count_harvest_recursive():
    rep(int(input("Days until harvest: ")))
    print("Harvest time!")
