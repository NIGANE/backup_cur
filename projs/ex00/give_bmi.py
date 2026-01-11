def give_bmi(
        height: list[int | float],
        weight: list[int | float]
) -> list[int | float]:
    re = []
    i = 0
    if not isinstance(height, list) or not isinstance(weight, list):
        return None
    if (len(height) != len(weight)):
        return None
    while i < len(height):
        if (height[i] <= 0):
            return None
        re.append(weight[i] / (height[i] ** 2))
        i += 1
    return re
