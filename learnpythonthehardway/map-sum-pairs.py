# Implement a MapSum class with insert, and sum methods.
#
# For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer
# represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.
#
# For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the
# pairs' value whose key starts with the prefix.
#
# Example 1:
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.leaves = {}
        self.map = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_word = True

    def setMap(self, map):
        self.map = map

    def getSum(self, prefix):
        cur, cnt = self.root, 0
        for c in prefix:
            if c in cur.leaves:
                cur = cur.leaves[c]  # bugfixed how do you know c for sure in cur.leaves?
                # if cur.is_word:  # bugfixed should not do this, if aa = 2 aaa = 3, when prefix is aaa,
                # we should not add 'aa' value
                #     cnt += self.map.get(temp, 0)  # knowledge notice usage of 'get' with 'default value'
            else:  # if c in prefix but not in trie,illegal
                return 0

        que = [(cur, prefix)]
        while que:
            cur, str = que.pop(0)
            if cur.is_word:
                cnt += self.map.get(str, 0)

            for t in cur.leaves:
                que.append((cur.leaves[t], str + t))

        return cnt


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        self.map = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.map[key] = val
        self.trie.insert(key)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        self.trie.setMap(self.map)
        return self.trie.getSum(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

if __name__ == '__main__':
    s = MapSum()
    s.insert("apple", 5)
    print s.sum('ap')
    s.insert('app', 3)
    print s.sum('ap')
    print s.sum('ab')
