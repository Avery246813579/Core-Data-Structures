from hashtable import HashTable


class Set:
    def __init__(self, elements=None):
        """ Creates a set with elements if set

        Time:
            Best: O(1)
            Worst: O(n)
                n: number of elements

        Space:
            Average: O(1)

        :param elements:    Iterator of what you want to add to the set
        """
        self.data = HashTable()
        self.size = 0

        if elements is None:
            return

        for element in elements:
            self.add(element)

    def __iter__(self):
        """ Iterator for our set """
        return iter(self.data.keys())

    def __str__(self):
        """ String representation """
        return str(self.data.keys())

    def __repr__(self):
        """ Rep the set """
        return "[Set: %]".format(str(self.values()))

    def add(self, element):
        """ Adds an element to our set. If it's already in the set we don't do anything

        Time:
            Best: O(1) - When we have no elements in our target bucket
            Worst: O(n) - When our element is not in our target bucket
        Space:
            Average: O(1)

        :param element:     Element we want to add to our set
        """

        # If the element is in our set we don't do anything
        if self.contains(element):
            return

        # Add element to our hash table and increase size
        self.data.set(element, None)
        self.size += 1

    def contains(self, element):
        """ Checks if an element is in our set

        Time:
            Best: O(1) - When we have no elements in our target bucket
            Worst: O(n) - When our element is not in our target bucket
        Space:
            Average: O(1)

        :param element:     Element we want to check if it's in our set
        """
        return self.data.contains(element)

    def remove(self, element):
        """ Removes an element from our set if it exists, or raises an error if it doesn't

        Time:
            Best: O(1) - When we have no elements in our target bucket
            Worst: O(n) - When our element is not in our target bucket
        Space:
            Average: O(1)

        :param element:     Element we want to delete from our set
        """

        # If the element is not in our set raise an error
        if not self.contains(element):
            raise KeyError

        # Delete the element and decrement our size
        self.data.delete(element)
        self.size -= 1

    def union(self, other_set):
        """ Gets the union of self set and another (all the unique elements)

        Time:
            Average: O(n)
        Space:
            Average: O(n)
                n - The number of elements in both self set and other_set

        :param other_set:     The set we want to union with
        """

        # Clone our current set
        clone = Set(self.values())

        # Try and add all the elements from the other set
        for element in other_set:
            clone.add(element)

        # Return our clone
        return clone

    def intersection(self, other_set):
        """ Gets the intersection of self set and other_set (elements the reoccur)

        Time:
            Average: O(n)
        Space:
            Average: O(n)
                n - The number of elements that intersect

        :param other_set:     The set we want to get the intersection with
        """

        # Create a new set
        new_set = Set()

        # For all the elements in our other_set, if it's inside self set, then we add it to our new set
        for element in other_set:
            if self.contains(element):
                new_set.add(element)

        # Return the new intersection set
        return new_set

    def difference(self, other_set):
        """ Gets the different of self set and other_set (self - other_set)

        Time:
            Average: O(n)
        Space:
            Average: O(n)
                n - The number of different elements

        :param other_set:     The set we want to get the difference with
        """

        # Create a new set to store difference in
        new_set = Set()

        # For all the elements in this set, if the other set doesn't have an element in our set, add it to the new set
        for element in self:
            if not other_set.contains(element):
                new_set.add(element)

        # Return difference set
        return new_set

    def is_subset(self, other_set):
        """ Checks if other_set is a subset of self set

        Time:
            Average: O(n)
                n - Number of elements in other_set
        Space:
            Average: O(1)

        :param other_set:     The set we want to check if subset of
        """

        # For all the elements in the other set, if one element is not in self set, other set will not be an
        # intersection
        for element in other_set:
            if not self.contains(element):
                return False

        # We are not not an subset which makes us an intersection
        return True

    def values(self):
        """ Get all the values from our set """
        return self.data.keys()
