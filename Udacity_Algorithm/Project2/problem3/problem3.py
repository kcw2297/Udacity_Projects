import sys
import heapq


class huffman_node:
    def __init__(self,char,freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __gt__(self, other):
        if not other:
            return -1
        if not isinstance(other, huffman_node):
            return -1
        return self.freq > other.freq

class huffman_coding():
    def huffman_encoding(self,data):
        if data == "":
            data = "Please re-enter the data"
        char_dic = self.text_to_frequency(data)
        min_heap = self.node_heap(char_dic)
        merged_root = self.merge_heap(min_heap)
        tree = heapq.heappop(merged_root)
        encoded = self.node_encode(tree)
        compressed_text = self.get_encoded_text(data,encoded)
        return compressed_text, tree


    def huffman_decoding(self,encode_text,tree):
        decode_text = ""

        if encode_text is None:
            return ""

        current_node = tree

        for char in encode_text:
            if char == "0":
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node.char is not None:
                decode_text += current_node.char
                current_node = tree
        return decode_text


    def text_to_frequency(self,data):
        char_dic = dict()
        for char in data:
            if not char in char_dic:
                char_dic[char] = 0
            else:
                char_dic[char] += 1
        return char_dic

    def node_heap(self,frequency):
        heap = []
        for key in frequency:
            node = huffman_node(key, frequency[key])
            heapq.heappush(heap,node)
        return heap


    def merge_heap(self,heap):
        if len(heap) == 1:
            node = heapq.heappop(heap)
            new_node = huffman_node(None, node.freq)
            new_node.left = node
            heapq.heappush(heap, new_node)
        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)

            new_node = huffman_node(None,node1.freq+node2.freq)
            new_node.left = node1
            new_node.right = node2

            heapq.heappush(heap,new_node)
        return heap

    def node_encode(self,tree):
        if tree.left is None and tree.right is None:
            return {tree.char:'0'}
        return self.node_encode_recursion(tree,"")

    def node_encode_recursion(self, root, current_code):
        codes = {}

        if root is None:
            return {}

        if root is not None:
            codes[root.char] = current_code


        codes.update(self.node_encode_recursion(root.left,current_code + "0"))
        codes.update(self.node_encode_recursion(root.right,current_code + "1"))
        return codes


    def get_encoded_text(self, text, encode):
        compressed_text = ""
        for x in text:
            compressed_text += encode[x]
        return compressed_text


# Testing


if __name__ == "__main__":

    huffman = huffman_coding()

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman.huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


    # Testing one letter
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman.huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Testing upper and lower case
    a_great_sentence = "AAAAAAAAA"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman.huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
