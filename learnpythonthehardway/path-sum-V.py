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


class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nodes = [[-1 for _ in xrange(5)] for _ in xrange(10)]
        for n in nums:
            nodes[n / 100][(n % 100) / 10] = n % 10

        res = [nodes[1][1]]
        res = self.traverse(nodes, 1, 1, res)
        return res[0]

    def traverse(self, nodes, i, j, res):
        if i == 4 and nodes[i][j] != -1:
            return nodes[i][j]
        if nodes[i][j] != -1 and nodes[i + 1][2 * j - 1] == -1 and nodes[i + 1][2 * j] == -1:
            return nodes[i][j]
        res[0] += self.traverse(nodes, i + 1, 2 * j - 1, res)
        res[0] += self.traverse(nodes, i + 1, 2 * j, res)
        return res


if __name__ == '__main__':
    print Solution().pathSum([113, 215, 221])
