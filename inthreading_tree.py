class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.ltag = 0  # 左标志，0 表示指向左子树，1 表示指向前驱
        self.rtag = 0  # 右标志，0 表示指向右子树，1 表示指向后继
def inthreading(p, pre):
    if p:
        inthreading(p.left, pre)
        p.ltag = 0 if p.left else 1
        p.rtag = 0 if p.right else 1
        if pre:
            if pre.rtag == 1:
                pre.right = p
            if p.ltag == 1:
                p.left = pre
        pre = p
        inthreading(p.right, pre)

# 中序遍历线索化二叉树的函数
def inorder_traversal_threaded(root):
    curr = root
    while curr:
        while curr.ltag == 0:
            curr = curr.left
        print(curr.value, end=" ")
        while curr.rtag == 1 and curr.right:
            curr = curr.right
            print(curr.value, end=" ")
        curr = curr.right
# 测试函数
def test_inorder_threading():
    # 构建二叉树
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    pre = None
    inthreading(root, pre)
    print("中序线索化遍历结果:")
    inorder_traversal_threaded(root)

test_inorder_threading()