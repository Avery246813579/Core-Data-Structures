#!python
from collections import deque

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
        """ Removes an item or returns a ValueError

        Time:
            Average: O(n)
        Space:
            Average: O(n)


        """

        # Let's get our node and parent
        node, parent = self._find_node_with_parent(item)

        # If we can't find the value then we cry THEN throw a ValueError
        if node is None:
            raise ValueError

        # It exists so we decrement the size
        self.size -= 1

        # If we have no children remove the bond with our family :'(
        if node.is_leaf():
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None

        # We have two children <3. We need to find our successor and he is now our nodes data. We break our successor's
        # bond in the _find_successor method
        elif node.is_full_branch():
            successor = self._find_successor(node)
            node.data = successor.data

        # We have one child!
        else:
            # Get the node we want to swap
            next_node = node.left
            if next_node is None:
                next_node = node.right

            # If we have no parent our new home is the root
            if parent is None:
                self.root = next_node
                return

            # We move the next_node up
            if parent.left == node:
                parent.left = next_node
            else:
                parent.right = next_node

    @staticmethod
    def _find_successor(node, current):
        """ Finds the successor of a node. The farthest right node :)

        Time:
            Best: O(1)
            Worst: O(n)

        Space:
            Average: O(1)
        """

        if node.left.data < current.data:



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

    def _find_node_recursive(self, item, node=-1):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        if node == -1:
            node = self.root

        if node is None:
            return None

        if node.data == item:
            return node
        elif node.data > item:
            return self._find_node_recursive(item, node.left)
        else:
            return self._find_node_recursive(item, node.right)

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

    def _find_node_with_parent(self, item):
        """ Returns a parent and child """

        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            if item == node.data:
                # Return the parent of the found node
                return node, parent
            elif item < node.data:
                parent = node
                node = node.left
            elif item > node.data:
                parent = node
                node = node.right
        # Not found
        return None, parent

    def _find_parent_node_recursive(self, item, node=-1, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        if node == -1:
            node = self.root

        if node is None:
            return None

        if item == node.data:
            return parent
        elif item < node.data:
            return self._find_parent_node_recursive(item, node.left, node)
        else:
            return self._find_parent_node_recursive(item, node.right, node)

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) Going to all the nodes?
        TODO: Memory usage: O(1) All the time?"""

        # Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_in_order_recursive(node.left, visit)

        # Visit this node's data with given function
        visit(node.data)

        # Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) Going to all the nodes?
        TODO: Memory usage: O(1) All the time?"""
        visit(node.data)

        if node.left is not None:
            self._traverse_pre_order_recursive(node.left, visit)

        if node.right is not None:
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) Going to all the nodes?
        TODO: Memory usage: O(1) All the time?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) Going to all the nodes?
        TODO: Memory usage: O(1) All the time?"""
        if node.left is not None:
            self._traverse_post_order_recursive(node.left, visit)

        if node.right is not None:
            self._traverse_post_order_recursive(node.right, visit)

        visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) Going to all the nodes?
        TODO: Memory usage: O(1) All the time?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.

        Running time: O(n) Going to all the nodes?
        Memory usage: O(n) Adding all the nodes to a queue
        """
        # Create queue to store nodes not yet traversed in level-order
        queue = deque([start_node])
        # Loop until queue is empty
        while len(queue) > 0:
            # Dequeue node at front of queue
            node = queue.popleft()
            # Visit this node's data with given function
            visit(node.data)
            # Enqueue this node's left child, if it exists
            if node.left is not None:
                queue.append(node.left)
            # Enqueue this node's right child, if it exists
            if node.left is not None:
                queue.append(node.right)


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

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
