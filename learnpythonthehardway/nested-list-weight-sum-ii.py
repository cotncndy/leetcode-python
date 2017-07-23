# Time:  O(n)
# Space: O(h)

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

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """

        def helper(nestedList, depth, res):
            if len(res) < depth + 1:
                res.append(0)
            if nestedList.isInteger():
                res[depth] += nestedList.getInteger()
            else:
                for i in nestedList:
                    helper(i, depth + 1, res)

        res = []
        for l in nestedList:  # bugfixed, don't forget this
            helper(l, 0, res)

        # [1,2,3,4] 4 * 1 + 3 * 2+ 2 * 3 + 1 * 4
        sum = 0
        for i in reversed(xrange(len(res))):
            sum += res[i] * (len(res) - i)

        return sum

    def depthSumInverse2(self, nestedList):
        weighted, un_weighted = 0, 0

        while nestedList:
            next_level = []
            for i in nestedList:
                if i.isInteger():
                    un_weighted += i.getInteger()
                else:
                    next_level.extend(i.getList())
            nestedList = next_level
            weighted += un_weighted

        return weighted
