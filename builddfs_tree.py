from typing import List, Dict, Union

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(preorder: List[int], inorder_map: Dict[int, int], i: int, l: int, r: int) -> Union[TreeNode, None]:
    """构建二叉树：分治"""
    if l > r:
        return None
    # 初始化根节点
    root_val = preorder[i]
    root = TreeNode(root_val)
    # 查询m，从而划分左右子树
    m = inorder_map[root_val]
    # 计算右子树的起始索引，即左子树的节点数加1
    right_start = m + 1
    # 递归构建左子树和右子树
    root.left = dfs(preorder, inorder_map, i + 1, l, m - 1)
    root.right = dfs(preorder, inorder_map, i + (m - l + 1), right_start, r)
    return root

def build_tree(preorder: List[int], inorder: List[int]) -> Union[TreeNode, None]:
    """构建二叉树"""
    inorder_map = {val: i for i, val in enumerate(inorder)}
    return dfs(preorder, inorder_map, 0, 0, len(inorder) - 1)

def inorder_traversal(root: TreeNode) -> List[int]:
    """中序遍历二叉树"""
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def preorder_traversal(root: TreeNode) -> List[int]:
    """先序遍历二叉树"""
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


