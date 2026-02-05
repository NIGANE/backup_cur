def sort(items: list) -> list:
    for ind in range(len(items)):
        min_index = ind

        for j in range(ind + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j

        items[ind], items[min_index] = items[min_index], items[ind]
    return items


arr = [-54, 432, 4, 5-4, 443, -234]
print(sort(arr))