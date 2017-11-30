#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Time: O(n)
    """
    # Check that all adjacent items are in order, return early if not
    for i in range(1, len(items)):
        last_item = items[i - 1]
        current_item = items[i]

        if current_item < last_item:
            return False

    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Time:
        Best: O(n)
        Worst: O(n^2)
    """
    max_index = len(items)

    # Repeat until all items are in sorted order
    while not is_sorted(items):

        # Swap adjacent items that are out of order
        for i in range(1, max_index):
            last_item = items[i - 1]
            current_item = items[i]

            if last_item > current_item:
                items[i - 1] = current_item
                items[i] = last_item

        max_index -= 1



def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Time:
        Best: O(n long n)
        Worst: O(n^2)
    """
    left_window = 0

    # Repeat until all items are in sorted order
    while not is_sorted(items):
        minimum = items[left_window]
        minimum_index = left_window

        # Find minimum item in unsorted items
        for i in range(left_window + 1, len(items)):
            if minimum > items[i]:
                minimum = items[i]
                minimum_index = i

        # Swap it with first unsorted item
        items[minimum_index] = items[left_window]
        items[left_window] = minimum

        left_window += 1



def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order."""

    pivot = 0
    # Repeat until all items are in sorted order
    while not is_sorted(items):
        # Take first unsorted item
        for i in range(pivot, 0, -1):
            item = items[i]
            next_item = items[i - 1]

            if next_item < item:
                break

            # Insert it in sorted order in front of items
            items[i] = next_item
            items[i - 1] = item

        pivot += 1

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.

    TODO: Running time: O(n)
    TODO: Memory usage: O(n)
    """

    # Create a new list
    new_list = [0] * (len(items1) + len(items2))

    # We merged it
    merge_helper(items1, items2, new_list)

    return new_list


def merge_helper(items1, items2, new_list):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.

    Running time: O(n)
    Memory usage: O(1)
    """

    left_pivot = 0
    right_pivot = 0
    index = 0

    # Go until we need it to stop
    while True:
        # If the left array is empty
        if left_pivot >= len(items1):
            new_list[index:] = items2[right_pivot:]
            break

        # If the right array is empty
        if right_pivot >= len(items2):
            new_list[index:] = items1[left_pivot:]
            break

        # If the left item is greater add the right item and move it's index
        if items1[left_pivot] > items2[right_pivot]:
            new_list[index] = items2[right_pivot]
            right_pivot += 1
        else:  # The right item is greater add the left item and move it's index
            new_list[index] = items1[left_pivot]
            left_pivot += 1

        index += 1


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.

    TODO: Running time: O(n^2)
    TODO: Memory usage: O(n)
    """
    # Buy my mix tape
    half = len(items) // 2

    # Split items list into approximately equal halves
    left_half = items[:half]
    right_half = items[half:]

    # Sort each half using any other sorting algorithm
    selection_sort(left_half)
    selection_sort(right_half)

    # Merge sorted halves into one list in sorted order
    return merge(left_half, right_half)

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.

    TODO: Running time: O(n log n)
    TODO: Memory usage: O(n log n)????
    """

    # Check if list is so small it's already sorted (base case)
    if len(items) < 2:
        return items

    # Split items list into approximately equal halves
    half = len(items) // 2
    left_half = items[:half]
    merge_sort(left_half)

    right_half = items[half:]

    # Sort each half by recursively calling merge sort
    merge_sort(right_half)

    # Merge sorted halves into one list in sorted order
    merge_helper(left_half, right_half, items)

def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    # main()
    ...