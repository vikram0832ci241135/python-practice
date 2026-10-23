import heapq
from itertools import count


class HuffmanNode:
    def __init__(self, character=None, frequency=0, left=None, right=None):
        self.character = character
        self.frequency = frequency
        self.left = left
        self.right = right


def huffman_coding(frequencies):
    order = count()
    queue = [(frequency, next(order), HuffmanNode(character, frequency)) for character, frequency in sorted(frequencies.items())]
    heapq.heapify(queue)
    while len(queue) > 1:
        _, _, left = heapq.heappop(queue)
        _, _, right = heapq.heappop(queue)
        parent = HuffmanNode(frequency=left.frequency + right.frequency, left=left, right=right)
        heapq.heappush(queue, (parent.frequency, next(order), parent))
    codes = {}

    def build_codes(node, code):
        if node.left is None and node.right is None:
            codes[node.character] = code
            return
        build_codes(node.left, code + "0")
        build_codes(node.right, code + "1")

    if queue:
        build_codes(queue[0][2], "")
    return codes


def main():
    frequencies = {"a": 5, "b": 9, "c": 12, "d": 13, "e": 16, "f": 45}
    print("Huffman Codes:")
    for character, code in sorted(huffman_coding(frequencies).items()):
        print(f"{character} -> {code}")


if __name__ == "__main__":
    main()
