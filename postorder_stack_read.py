class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    if not root:
        return []

    s = []
    cur = root
    pre = None
    result = []

    while cur or s:
        while cur:
            s.append(cur)
            cur = cur.left  # 先遍历左子树

        # 当栈不为空，弹出栈顶元素
        cur = s.pop()
        # 如果当前节点的右子节点为空或者右子节点已经被访问过（即右子节点是pre）
        if cur.right is None or pre == cur.right:
            result.append(cur.val)  # 访问当前节点
            pre = cur  # 更新pre为当前节点
            cur = None  # 避免访问当前节点的右子树
        else:
            # 将当前节点再次压入栈中，并转向右子树
            s.append(cur)
            cur = cur.right

    return result

# 测试代码
if __name__ == "__main__":
    # 构建一个简单的二叉树
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Post-order traversal:", postorderTraversal(root))