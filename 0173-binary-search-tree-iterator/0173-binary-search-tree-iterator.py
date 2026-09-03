class BSTIterator(object):

    def __init__(self, root):
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        node = self.stack.pop()

        right_node = node.right

        while right_node:
            self.stack.append(right_node)
            right_node = right_node.left

        return node.val

    def hasNext(self):
        return len(self.stack) > 0