# Time:  O(n), n is the number of the integers.
# Space: O(h), h is the depth of the nested lists.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        self.stack = []
        for i in reversed(xrange(len(nestedList))):
            self.stack.append(nestedList[i])

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            res = self.stack[-1]
            if res.isInteger():
                return True
            self.stack.pop()
            for i in reversed(xrange(len(res.getList()))):
                self.stack.append(res.getList()[i])
        return False

    def next(self):
        """
        :rtype: int
        """
        res = self.stack.pop()
        return res.getInteger()
