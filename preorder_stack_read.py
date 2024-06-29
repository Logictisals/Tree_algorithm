class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def PreOrderNonRecursive(self):
        StackTreeNode = []
        tTreeNode = self.root
        while len(StackTreeNode) > 0 or tTreeNode is not None:
            while tTreeNode is not None:
                self.VisitBinaryTreeNode(tTreeNode)
                StackTreeNode.append(tTreeNode)
                tTreeNode = tTreeNode.left_child
            if len(StackTreeNode) > 0:
                tTreeNode = StackTreeNode.pop()
                tTreeNode = tTreeNode.right_child

    def VisitBinaryTreeNode(self, BinaryTreeNode):
        # 值为'#'的节点代表空节点
        if BinaryTreeNode.data != '#':
            print(BinaryTreeNode.data)

# 测试代码
if __name__ == "__main__":
    # 创建二叉树节点
    root = BinaryTreeNode(1)
    root.left_child = BinaryTreeNode(2)
    root.right_child = BinaryTreeNode(3)
    root.left_child.left_child = BinaryTreeNode(4)
    root.left_child.right_child = BinaryTreeNode(5)

    # 创建二叉树对象并进行前序遍历
    tree = BinaryTree(root)
    print("Pre-order traversal (non-recursive):")
    tree.PreOrderNonRecursive()