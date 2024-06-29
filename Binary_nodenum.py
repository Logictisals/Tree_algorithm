class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def num_of_nodes(t):
    # 如果当前节点为空，返回0
    if t is None:
        return 0
    # 否则，返回当前节点的值加上左子树和右子树中节点数的和
    else:
        return 1 + num_of_nodes(t.left) + num_of_nodes(t.right)

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

    # 计算二叉树中节点的个数
    count = num_of_nodes(root)
    print(f"The number of nodes in the tree is: {count}")