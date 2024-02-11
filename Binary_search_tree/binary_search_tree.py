import queue


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        pass

    def lookup(self, value):
        pass

    def remove(self, value):
        pass

    def breadth_first_search(self):
        if self.root is None:
            return []
        curr_node = self.root
        array = []
        q = queue.SimpleQueue()
        q.put(curr_node)

        while not q.empty():
            curr_node = q.get()
            array.append(curr_node.value)
            if curr_node.left:
                q.put(curr_node.left)
            if curr_node.right:
                q.put(curr_node.right)

        return array

    def depth_first_search_in_order(self):
        return self.traverse_in_order(self.root, [])

    def depth_first_search_pre_order(self):
        return self.traverse_pre_order(self.root, [])

    def depth_first_search_post_order(self):
        return self.traverse_post_order(self.root, [])

    def traverse_in_order(self, node, array):
        if node is None:
            return array
        if node.left:
            self.traverse_in_order(node.left, array)
        array.append(node.value)
        if node.right:
            self.traverse_in_order(node.left, array)
        return array

    def traverse_pre_order(self, node, array):
        if node is None:
            return array
        array.append(node.value)
        if node.left:
            self.traverse_pre_order(node.left, array)
        array.append(node.value)
        if node.right:
            self.traverse_pre_order(node.left, array)
        return array

    def traverse_post_order(self, node, array):
        if node is None:
            return array
        if node.left:
            self.traverse_post_order(node.left, array)
        array.append(node.value)
        if node.right:
            self.traverse_post_order(node.left, array)
        array.append(node.value)
        return array