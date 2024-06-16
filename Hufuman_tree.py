class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanTree:
    def __init__(self):
        self.heap = []

    def push(self, node):
        self.heap.append(node)
        self.heap.sort()  # 手动维持堆的特性

    def pop(self):
        return self.heap.pop(0)  # 弹出最小元素

    def merge_nodes(self):
        while len(self.heap) > 1:
            left = self.pop()
            right = self.pop()
            merged = HuffmanNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            self.push(merged)

    def build_huffman_tree(self, frequency):
        for key in frequency:
            self.push(HuffmanNode(key, frequency[key]))
        self.merge_nodes()
        return self.heap[0]  # 返回根节点

def calculate_frequencies(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def build_huffman_codes(root, code=""):
    if root is None:
        return {}
    if root.char is not None:
        return {root.char: code}
    return {
        **build_huffman_codes(root.left, code + "0"),
        **build_huffman_codes(root.right, code + "1")
    }

# 示例文本
text = "this is an example of a huffman tree"

# 计算频率
frequencies = calculate_frequencies(text)

# 创建哈夫曼树对象并构建哈夫曼树
huffman_tree = HuffmanTree()
root = huffman_tree.build_huffman_tree(frequencies)

# 生成哈夫曼编码
huffman_codes = build_huffman_codes(root)

# 打印结果
for char, code in huffman_codes.items():
    print(f"字符 '{char}' 编码为 '{code}'")