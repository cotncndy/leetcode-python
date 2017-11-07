# Implement a data structure supporting the following operations:
#
# Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty
# string.
# Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If
# the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
# GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
# GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
# Challenge: Perform all these in O(1) time complexity.
import collections


class Node(object):
    def __init__(self, val):
        self.val = val
        self.set = set()
        self.next, self.prev = None, None


class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = collections.defaultdict(Node)
        # place max on head, min on tail
        self.head, self.tail = Node(float('inf')), Node(float('-inf'))
        self.head.next, self.tail.prev = self.tail, self.head

    def insert(self, prev, after, node):
        prev.next, after.prev = node, node
        node.next, node.prev = after, prev

    def delete(self, cur):
        cur.prev.next, cur.next.prev = cur.next, cur.prev
        cur.next, cur.prev = None, None

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key not in self.map:
            if self.head.next.val != 1:  # if it is empty deque
                t = Node(1)
                t.set.add(key)
                self.insert(self.head, self.head.next, t)
            else:  # insert the key to Node(1)
                t = self.head.next
                t.set.add(key)

            self.map[key] = t
        else:
            t = self.map[key]
            if t.next.val == t.val + 1:
                t.next.set.add(key)  # add key to node(+1)
                self.map[key] = t.next
            else:
                k = Node(t.val + 1)
                k.set.add(key)
                self.insert(t, t.next, k)
                self.map[key] = k
            t.set.remove(key)  # remove key from node()
            if not len(t.set):  # if t is empty now, we should remove it
                self.delete(t)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.map:
            return

        t = self.map[key]
        if t.val > 1:
            if t.prev.val == t.val - 1:
                t.prev.set.add(key)
                self.map[key] = t.prev
            else:
                k = Node(t.val - 1)
                k.set.add(key)
                self.insert(t.prev, t, k)
                self.map[key] = k

        t.set.remove(key)
        if not len(t.set):
            self.delete(t)
        if t.val == 1:  # bugfixed, this little sucker, waste me a lot of time
            del self.map[key]

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return next(iter(self.tail.prev.set)) if len(self.tail.prev.set) > 0 else ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        return next(iter(self.head.next.set)) if len(self.head.next.set) > 0 else ""


if __name__ == '__main__':
    obj = AllOne()
    obj.inc("a")
    # obj.inc("b")
    # obj.inc("b")
    # obj.inc("c")
    # obj.inc("c")
    # obj.inc("c")
    # obj.dec("b")
    # obj.dec("b")
    print obj.getMinKey()
    obj.dec('a')
    obj.inc('c')
    print obj.getMaxKey()
    print obj.getMinKey()




    # Your AllOne object will be instantiated and called as such:
    # obj = AllOne()
    # obj.inc(key)
    # obj.dec(key)
    # param_3 = obj.getMaxKey()
    # param_4 = obj.getMinKey()
