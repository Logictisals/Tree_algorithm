def creatfmt(nodes,low , high):
    if low <high:
        mid= (low +high) //2
        s = Tree(nodes[mid])#生成一个新的节点
        s.lchild =creatfmt(nodes,low , mid-1)
        s.rchild = creatfmt(nodes,mid+1,high)
        return s
    return None
class Tree:
    def __init__(self,data):
        self.data = data
        self.rchild=None
        self.lchild=None
def creat_tree_from_list(node_list):
    return creatfmt(node_list,0,len(node_list)-1)
nodes = [1,2,3,4,5,6]
newTree=creat_tree_from_list(nodes)
print(newTree)
def print_tree(tree_node):
    if tree_node is None:
        return
    print_tree(tree_node.lchild)
    print(tree_node.data,end=' ')
    print_tree(tree_node.rchild)
print_tree(newTree)
