class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def InOrderNonRecursive(self):
        StackTreeNode = []
        tTreeNode = self.root
        while len(StackTreeNode) > 0 or tTreeNode is not None:
            while tTreeNode is not None:
                StackTreeNode.append(tTreeNode)
                tTreeNode = tTreeNode.left  # 这里应该是小写的left，不是LeftChild
            if len(StackTreeNode) > 0:
                tTreeNode = StackTreeNode.pop()
                self.VisitBinaryTreeNode(tTreeNode)
                tTreeNode = tTreeNode.right  # 同上，应该是right

    def VisitBinaryTreeNode(self, BinaryTreeNode):
        # 打印非空节点的值
        print(BinaryTreeNode.data)

# 测试代码
if __name__ == "__main__":
    # 构建一个简单的二叉树
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)

    tree = BinaryTree(root)
    print("In-order traversal (non-recursive):")
    tree.InOrderNonRecursive()