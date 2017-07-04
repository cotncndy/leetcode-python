# Time:  O(1), per operation.
# Space: O(k), k is the capacity of cache.

# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and set.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
#
# set(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.list = DoubleLinkedList()
        self.dict = {}
        self.capacity = capacity

    def __insert(self, key, val):
        node = ListNode(key, val)
        self.list.append(node)
        self.dict[key] = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            val = self.dict[key].val
            self.list.delete(self.dict[key])
            self.__insert(key, val)
            return val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            self.delete(self.dict[key])
        elif len(self.dict) == self.capacity:
            del self.dict[self.list.head.key]
            self.list.delete(self.list.head)

        self.__insert(key, value)


        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
