class TreeNode(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = "TreeNode(data={}, left={}, right={})"
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree(object):
    def __init__(self, tree_data: list):
        # root must be set outside of recursion
        self.root = TreeNode(tree_data[0], None, None)
        for d in tree_data[1:]:
            self.insert(self.root, d)

    def data(self):
        return self.root

    def sorted_data(self):
        return self.traverse(self.root, [])

    def insert(self, node: type(TreeNode), data: str):
        if data <= node.data:
            if node.left:
                self.insert(node.left, data)
            else:
                node.left = TreeNode(data, None, None)
        else:
            if node.right:
                self.insert(node.right, data)
            else:
                node.right = TreeNode(data, None, None)

    def traverse(self, node: type(TreeNode), result: list):
        if node:
            result = self.traverse(node.left, result)
            result.append(node.data)
            result = self.traverse(node.right, result)

        return result
