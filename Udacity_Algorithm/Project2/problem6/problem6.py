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
        if self.head is None:
            return "There is empty list"
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

def union(llist_1, llist_2):
    node = llist_1.head
    if node is None:
        return llist_2

    while node.next:
        node = node.next
    node.next = llist_2.head
    return llist_1


def intersection(llist_1, llist_2):
    intersection = LinkedList()
    temp_dic = {}
    node = llist_1.head
    while node:
        if node.value not in temp_dic:
            temp_dic[node.value] = 0
        temp_dic[node.value] += 1
        node = node.next

    node = llist_2.head
    while node:
        if node.value in temp_dic:
            new_node = Node(node.value)
            intersection.append(new_node)
            temp_dic[node.value] -= 1
            if temp_dic[node.value] < 1:
                del temp_dic[node.value]
        node = node.next

    return intersection



# Testing


linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))




linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))




linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
