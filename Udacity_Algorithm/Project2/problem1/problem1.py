class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.previous = None

class LRU_Cache(object):

    def __init__(self, capacity):
        self.head = Node("head","head")
        self.tail = Node("tail","tail")
        self.head.next = self.tail
        self.tail.previous = self.head
        self.max_size = capacity
        self.curr_size = 0
        self.dic = {}


    def removeNode(self, node):
        # Remove the node and connect previous and next node
        prev_node, next_node = node.previous, node.next
        prev_node.next, next_node.previous = node.next, node.previous


    def moveToFront(self, node):
        # Move the node to the front(in front of head node)
        next_node = self.head.next
        node.next = next_node
        next_node.previous = node
        node.previous = self.head
        self.head.next = node



    def get(self, key):
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.removeNode(node) #Remove the node in order to move to the front
        self.moveToFront(node) #Move the recent used node to the front
        return node.val



    def set(self, key, val):
        if self.max_size <= 0:
            return None
        if key in self.dic:
            node = self.dic[key]
            node.val = val
            self.removeNode(node)
            self.moveToFront(node)
        else:
            if self.curr_size >= self.max_size:
                old_node = self.tail.previous
                del self.dic[old_node.key]
                self.removeNode(old_node)
                self.curr_size -= 1

            new_node = Node(key,val)
            self.dic[key] = new_node
            self.moveToFront(new_node)
            self.curr_size += 1


# Testing

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Test 2
our_cache = LRU_Cache(0)
our_cache.set(1, 1);
our_cache.get(1) # returns -1, because there is no capacity to save data

# Test 3
our_cache = LRU_Cache(-1)
our_cache.set(1, 1);
our_cache.get(1) # returns -1, because capacity is minus
