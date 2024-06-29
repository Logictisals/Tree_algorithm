class CircularSequenceQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0

    def InitQueue(self):
        self.head = 0
        self.tail = 0

    def IsEmptyQueue(self):
        return self.head == self.tail

    def EnQueue(self, item):
        if (self.tail + 1) % self.capacity == self.head:
            raise Exception("Queue is full")
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity

    def DeQueue(self):
        if self.IsEmptyQueue():
            raise Exception("Queue is empty")
        item = self.queue[self.head]
        self.head = (self.head + 1) % self.capacity
        return item

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def VisitBinaryTreeNode(self, BinaryTreeNode):
        print(BinaryTreeNode.data)

    def LevelOrder(self, Root):
        if Root is None:
            return
        tSequenceQueue = CircularSequenceQueue(100)
        tSequenceQueue.InitQueue()
        tSequenceQueue.EnQueue(Root)
        while not tSequenceQueue.IsEmptyQueue():
            tTreeNode = tSequenceQueue.DeQueue()
            self.VisitBinaryTreeNode(tTreeNode)
            if tTreeNode.left is not None:
                tSequenceQueue.EnQueue(tTreeNode.left)
            if tTreeNode.right is not None:
                tSequenceQueue.EnQueue(tTreeNode.right)

# 测试代码
if __name__ == "__main__":
    # 构建一个简单的二叉树
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)

    tree = BinaryTree()
    print("Level-order traversal:")
    tree.LevelOrder(root)