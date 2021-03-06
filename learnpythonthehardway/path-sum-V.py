# If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.
#
# For each integer in this list:
# The hundreds digit represents the depth D of this node, 1 <= D <= 4.
# The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the
# same as that in a full binary tree.
# The units digit represents the value V of this node, 0 <= V <= 9.
# Given a list of ascending three-digits integers representing a binary with the depth smaller than 5. You need to
# return the sum of all paths from the root towards the leaves.
#
# Example 1:
# Input: [113, 215, 221]
# Output: 12
# Explanation:
# The tree that the list represents is:
#     3
#    / \
#   5   1
#
# The path sum is (3 + 5) + (3 + 1) = 12.
# Example 2:
# Input: [113, 221]
# Output: 4
# Explanation:
# The tree that the list represents is:
#     3
#      \
#       1
#
# The path sum is (3 + 1) = 4.
import collections


class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nodes = [[-1 for _ in xrange(10)] for _ in xrange(5)]
        for n in nums:
            nodes[n / 100][(n % 100) / 10] = n % 10

        res, temp = [], []
        self.traverse(nodes, 1, 1, temp, res)
        suma = 0
        for t in res:
            suma += sum(t)
        return suma

    def traverse(self, nodes, i, j, temp, res):
        if nodes[i][j] == -1:
            return
        temp.append(nodes[i][j])
        if i == 4 and nodes[i][j] != -1:
            res.append(temp)
            return
        if nodes[i][j] != -1 and nodes[i + 1][2 * j - 1] == -1 and nodes[i + 1][2 * j] == -1:
            res.append(temp)
            return
        t1 = temp[:]
        t2 = temp[:]
        self.traverse(nodes, i + 1, 2 * j - 1, t1, res)
        self.traverse(nodes, i + 1, 2 * j, t2, res)

    def pathSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        i = n - 1
        table = collections.defaultdict(int)
        ans = 0
        while i >= 0:
            num = str(nums[i])
            level, position, value = int(num[0]), int(num[1]), int(num[2])
            key = (level, position)
            if key not in table:
                table[key] = 1
            ans += table[key] * value
            parent = (level - 1, (position + 1) / 2)
            table[parent] += table[key]
            i -= 1

        return ans

if __name__ == '__main__':
    # print Solution().pathSum([113, 215, 221])[115,215,224,325,336,446,458]
    # print Solution().pathSum([113, 221])
    print Solution().pathSum([115, 215, 224, 325, 336, 446, 458])
