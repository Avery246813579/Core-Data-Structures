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
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # We set our left and right margin
    left = 0
    right = len(array) - 1

    # We can do a while True because we have a base case
    while True:
        # We get the width of the remaining elements between the margins
        width = right - left

        # If our width is less then 2 then we are at a margin
        if width < 2:
            # If we are at the left margin and our item is there, then return the left index
            if left == 0:
                if array[left] == item:
                    return left
            # If we are at the right margin and our item is there, then return the right index
            else:
                if array[right] == item:
                    return right

            # Return out if it's not our item. We don't have the item in our list
            return

        # Our new index is our left margin plus the remaining width divided by 2 (we get the middle of the remaining
        # elements)
        index = left + width // 2

        # If our current item is the item we are looking for return it back
        if array[index] == item:
            return index
        # If our item is less then our current item then let's move the left margin
        elif array[index] < item:
            left = index
        # If our item is more then our current item then let's move the right margin
        else:
            right = index


def binary_search_recursive(array, item, left=0, right=None):
    # If we don't have a right margin
    if right is None:
        right = len(array) - 1

    # Our new index is our left margin plus the remaining width divided by 2 (we get the middle of the remaining
    # elements)
    index = (left + right) // 2

    if left > right:
        return None

    # If our current item is the item we are looking for return it back
    if array[index] == item:
        return index
    # If our item is less then our current item then let's move the left margin
    elif array[index] < item:
        return binary_search_recursive(array, item, index + 1, right)
    # If our item is more then our current item then let's move the right margin
    else:
        return binary_search_recursive(array, item, left, index - 1)
