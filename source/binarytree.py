#!python


class BinaryTreeNode(object):
    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return not self.is_leaf()

    def is_full_branch(self):
        return self.left is not None and self.right is not None

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""

        if self.is_leaf():
            return 0

        # If we have a left leave then set the height to that leafs height
        if self.left is not None:
            height = self.left.height()

        # If we have a right leave
        if self.right is not None:
            # Get that right leafs height
            right_height = self.right.height()

            # If we didn't have a left leave or the right leaf is greater then the height is now the right height
            if height is None or right_height > height:
                height = right_height

        # Add one for fun (we need to increment for recursion)
        return height + 1


class BinarySearchTree(object):
    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).

        Time:
            Best: O(1) - If root is not set
            Worst: O(n) - Go through all children
        """
        if self.root is None:
            return 0

        return self.root.height

    def remove(self, item):
        node = self._find_node(item)

        # If we can't find the value then we cry
        if node is None:
            raise ValueError

        self.size -= 1
        parent = self._find_parent_node(item)

        # If we have no children remove the bond with our family :'(
        if node.is_leaf():
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None

            return

        # If the node we want to find has both a right and left child then we find the successor and set our node's
        # value to our successor. Our _find_successor already breaks our successor's bond with it's parent
        if node.is_full_branch():
            successor = self._find_successor(node)
            node.data = successor.data

            return

        # If we get here then we have one child

        # Get the node we want to swap
        if node.left is not None:
            next_node = node.left
        else:
            next_node = node.right

        # If we have no parent our new place is the root
        if parent is None:
            self.root = next_node
            return

        # Set our new place to the place
        if parent.left == node:
            parent.left = next_node
        else:
            parent.right = next_node

    def _find_successor(self, node):
        # Keep going until we have no right and then do it
        while node.right is not None:
            temp = node.right

            if temp.right is None:
                node.right = None
                return temp

            node = temp

    def contains(self, item):
        """Return True if this binary search tree contains the given item.

        Time:
            Best: O(1) - If tree is empty or only has a ehad
            Worst: O(n) - Have to check all nodes
        """
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        return node.data if self._find_node(item) else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Handle the case where the tree is empty
        if self.is_empty():
            self.root = BinaryTreeNode(item)
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node(item)
        if item < parent.data:
            parent.left = BinaryTreeNode(item)
        elif item > parent.data:
            parent.right = BinaryTreeNode(item)
        self.size += 1

    def _find_node(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            if node.data == item:
                # Return the found node
                return node
            elif item < node.data:
                node = node.left
            elif item > node.data:
                node = node.right
        # Not found
        return None

    def _find_parent_node(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            if item == node.data:
                # Return the parent of the found node
                return parent
            elif item < node.data:
                parent = node
                node = node.left
            elif item > node.data:
                parent = node
                node = node.right
        # Not found
        return parent

        # This space intentionally left blank (please do not delete this comment)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))


if __name__ == '__main__':
    test_binary_search_tree()
