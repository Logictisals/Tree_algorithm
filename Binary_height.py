def depth(t):
    if t is None:
        h = 0
    else:
        # 计算左子树的深度
        lh = depth(t.left)
        # 计算右子树的深度
        rh = depth(t.right)
        # 比较左子树和右子树的深度，取较大的一个加1作为当前节点的深度
        h = max(lh, rh) + 1
    return h

# 假设BinaryTreeNode类已经定义如下：
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

    # 计算二叉树的深度
    tree_depth = depth(root)
    print(f"The depth of the tree is: {tree_depth}")