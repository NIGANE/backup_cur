

# def mage_counter() -> callable:
#     if not hasattr(mage_counter, "count")
#         count = 0
#     count += 1
#     return lambda: count = count + 1

def test():
    x = 0

    def print_x():
        nonlocal x
        x += 1
        print(x)
    return print_x
test()()
test()()