class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def locate(t, x):
    # 如果当前节点为空，返回None
    if t is None:
        return None
    # 如果当前节点的数据等于要查找的值x，返回当前节点
    elif t.data == x:
        return t
    # 如果当前节点的数据不等于x，递归地在左子树和右子树中查找
    else:
        # 首先在左子树中查找
        p = locate(t.left, x)
        if p:
            return p
        # 如果左子树中没有找到，然后在右子树中查找
        else:
            return locate(t.right, x)

# 测试代码
if __name__ == "__main__":
    # 构建一个简单的二叉树
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)

    # 查找值为3的节点
    node = locate(root, 6)
    if node:
        print(f"Found node with value: {node.data}")
    else:
        print("Value not found in the tree.")