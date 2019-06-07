class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def parse(self):
        node = self.head
        while node:
            yield(node.value)
            node = node.next


def union(list_1, list_2):
    united = set()
    for i in list_1.parse():
        united.add(i)
    for i in list_2.parse():
        united.add(i)
    return(united)


def intersection(list_1, list_2):
    set_1 = set(x for x in list_1.parse())

    intersection = set()
    for i in list_2.parse():
        if i in set_1:
            intersection.add(i)
    return(intersection)


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("TEST CASE 1")
print("union returns the following:")
print (union(linked_list_1,linked_list_2))
print("intersection returns the following: ")
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)
print("TEST CASE 2")
print("union returns the following:")
print(union(linked_list_3, linked_list_4))
print("intersection returns the following: ")
print(intersection(linked_list_3, linked_list_4))


# Test case 3: (One set is empty)
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print("TEST CASE 3")
print("union returns the following:")
print(union(linked_list_5, linked_list_6))
print("intersection returns the following: (An empty set)")
print(intersection(linked_list_5, linked_list_6))
