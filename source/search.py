#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index > len(array) - 1:
        return None

    if array[index] == item:
        return index

    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left = 0
    right = len(array) - 1

    while True:
        width = right - left

        if width < 2:
            if left == 0:
                if array[left] == item:
                    return left
            else:
                if array[right] == item:
                    return right

            return

        index = left + width // 2

        if array[index] == item:
            return index
        elif array[index] < item:
            left = index
        else:
            right = index


def binary_search_recursive(array, item, left=0, right=None):
    if right is None:
        right = len(array) - 1

    print(left, right)
    width = right - left

    if width < 2:
        if left == 0:
            if array[left] == item:
                return left
        else:
            if array[right] == item:
                return right

        return

    index = left + width // 2

    if array[index] == item:
        return index
    elif array[index] < item:
        return binary_search_recursive(array, item, index, right)
    else:
        return binary_search_recursive(array, item, left, index)

