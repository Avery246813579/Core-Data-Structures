def increase(arr, index=None):
    if index is None:
        index = len(arr) - 1

    if index == -1:
        return [1] + arr

    arr[index] += 1

    if arr[index] != 10:
        return arr

    arr[index] = 0
    return increase(arr, index - 1)


assert increase([0]) == [1]
print(increase([0]))
assert increase([9]) == [1, 0]
print(increase([9]))
assert increase([1, 0]) == [1, 1]
print(increase([1, 0]))
assert increase([9, 9]) == [1, 0, 0]
print(increase([9, 9]))
