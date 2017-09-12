# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in
# nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of
# C. And we defined a friend circle is a group of students who are direct or indirect friends.
#
# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1,
# then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total
# number of friend circles among all the students.
#
# Example 1:
# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.
# Example 2:
# Input:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
# Note:
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.


class UnionFind(object):
    def __init__(self, n):
        self.__group = range(n)  # bugfixed
        self.size = n

    def find(self, x):
        while (x != self.__group[x]):
            self.__group[x] = self.__group[self.__group[x]]
            x = self.__group[x]  # bugfixed, forgot this one

        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.__group[min(x, y)] = max(x, y)
            self.size -= 1


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not len(M) or not len(M[0]):
            return 0
        n = len(M)

        union_find = UnionFind(n)
        for i in xrange(0, n):
            for j in xrange(i + 1, n):
                if M[i][j] == 1:
                    union_find.union(i, j)

        return union_find.size

    def recursive(self, index):
        for i, item in enumerate(self.M[index]):
            if item == 1 and i not in self.nums:
                self.nums.add(i)
                self.recursive(i)

    def findCircleNum2(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.nums = set()
        self.M = M
        count = 0
        for index in xrange(len(M)):
            if index not in self.nums:
                count += 1
                self.nums.add(index)
                self.recursive(index)
        return count


if __name__ == '__main__':
    print Solution().findCircleNum2([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    print Solution().findCircleNum2([[1, 1, 0, 0, 0, 0],
                                     [1, 1, 0, 0, 0, 0],
                                     [0, 0, 1, 1, 0, 0],
                                     [0, 0, 1, 1, 1, 0],
                                     [0, 0, 0, 1, 1, 0],
                                     [0, 0, 0, 0, 0, 1]])
