import sys


class Huffman_Node:

    def __init__(self):
        self.freq = None
        self.left = None
        self.right = None
        self.code = ""  # Code to be assigned to nodes below in the tree
        self.next = None  # Additional info to simplify ordered list
        self.data = (self.freq)  # Additional info to simplify ordered list printing


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.code = ""  # Code assignet to the char in this node
        self.freq = self.data[0]


class Ordered_List:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_node(self, new_node):
        if self.size == 0:
            self.head = new_node
        elif new_node.freq <= self.head.freq:
            # new node replaces the head
            new_node.next = self.head
            self.head = new_node
        else:
            # list is not empty and new node > head
            keep_traversing = True
            current_node = self.head
            while keep_traversing:
                if current_node.next:
                    if new_node.freq > current_node.next.freq:
                        current_node = current_node.next

                    else:
                        new_node.next = current_node.next
                        current_node.next = new_node
                        keep_traversing = False

                else:
                    current_node.next = new_node
                    keep_traversing = False
        self.size += 1

    def pop(self):
        if self.size > 0:
            output = self.head
            self.head = self.head.next
            self.size -= 1
            return(output)
        else:
            return(None)

    def print_list(self):
        output = []
        current_node = self.head
        while current_node:
            output.append(current_node.data)
            current_node = current_node.next
        print(output)


class Huffman_Tree:
    def __init__(self, input_string):
        self._input_string = input_string
        self.code_dict = {}
        self.root = self._build_tree()
        self._codify_tree(self.root, None)

    def _build_tree(self):
        # Count frequency of each character in the input string:
        dict = {}
        for i in self._input_string:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        # Store dict's information as a tuple list:
        tuplelist = []
        for key in dict.keys():
            tuplelist.append((dict[key], key))
        # Generate an ordered list:
        ord_list = Ordered_List()
        for i in tuplelist:
            new_node = ListNode(i)
            ord_list.add_node(new_node)
        # Additional clause in case list has only one char
        if ord_list.size == 1:
            # here we build manually a list with a root and a node
            manual_root = Huffman_Node()
            manual_root.left = ord_list.pop()
            manual_root.freq = manual_root.left.freq
            manual_root.data = (new_node.freq, "***")
            return(manual_root)
        # Use the List to generate a tree and return it's root
        while ord_list.size > 1:
            new_node = Huffman_Node()
            pop1 = ord_list.pop()
            pop2 = ord_list.pop()
            new_node.left = pop1
            new_node.right = pop2
            new_node.freq = pop1.freq + pop2.freq
            new_node.data = (new_node.freq, "***")
            ord_list.add_node(new_node)
        return(ord_list.pop())

    def _codify_tree(self, node, code):
        current_node = node
        if not current_node:
            return
        if code:
            current_node.code = code + current_node.code
        if hasattr(current_node, 'left'):
            self._codify_tree(current_node.left, current_node.code + '0')
        if hasattr(current_node, 'right'):
            self._codify_tree(current_node.right, current_node.code + '1')
        else:
            self.code_dict[current_node.data[1]] = current_node.code
        return


def Huffman_Encode(string, huff_tree):
    output = ""
    for char in string:
        code = huff_tree.code_dict[char]
        output = output + code
    return(output)

def Huffman_Decode(code, tree):
    if len(code) == 0:
        return("Warning, can't decode empty string")
    output = ""
    code_length = len(code) - 1
    index = 0
    current_node = tree.root
    while index <= code_length:
        if hasattr(current_node, 'right'):  # True if not a leaf
            if code[index] == '0':
                current_node = current_node.left
                index += 1
            elif code[index] == '1':
                current_node = current_node.right
                index += 1
        else:
            output += current_node.data[1]  #Get char from node and reset position
            current_node = tree.root
    if not hasattr(current_node, 'right'):  # Check last leaf
        output += current_node.data[1]
        return(output)
    else:
        return("ERROR: code unreadable")

#  --------------------------------TEST CASE 1-----------------------
a_great_sentence = "The bird is the word"

print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))

tree = Huffman_Tree(a_great_sentence)
encoded_data = Huffman_Encode(a_great_sentence, tree)
print("The size of the encoded data is: {}".format(sys.getsizeof(encoded_data)))
print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
print("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = Huffman_Decode(encoded_data, tree)

print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
print("The content of the encoded data is: {}\n".format(decoded_data))
#  --------------------------------TEST CASE 2-----------------------"""
print("TEST CASE 2: Someone wants to codify screaming")

a_great_sentence = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))

tree = Huffman_Tree(a_great_sentence)
encoded_data = Huffman_Encode(a_great_sentence, tree)

print("The size of the encoded data is: {}".format(encoded_data))#(sys.getsizeof(int(encoded_data, base=2))))
print("Size")
print("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = Huffman_Decode(encoded_data, tree)

print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
print("The content of the encoded data is: {}\n".format(decoded_data))
#  --------------------------------TEST CASE 3-----------------------
print("TEST CASE 3: EMPTY STRING")

a_great_sentence = ""

print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))

tree = Huffman_Tree(a_great_sentence)
encoded_data = Huffman_Encode(a_great_sentence, tree)


decoded_data = Huffman_Decode(encoded_data, tree)

print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
print("The content of the encoded data is: {}\n".format(decoded_data))
