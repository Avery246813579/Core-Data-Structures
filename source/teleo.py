from collections import OrderedDict

class Price:
    def __init__(self, file):
        file_reader = open(file)

        lines = file_reader.read().splitlines()

        pricing = {}
        for line in lines:
            split = line.split(",")

            pricing[split[0]] = float(split[1])

        self.pricing = OrderedDict(sorted(pricing.items()))

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


if __name__ == "__main__":
    price = Price('../routes/route-costs-10.txt')
    print((binary_search_recursive(price.pricing.keys(), '+14105547746')))
