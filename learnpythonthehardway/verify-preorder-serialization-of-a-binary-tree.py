# Time:  O(n)
# Space: O(1)

# One way to serialize a binary tree is to use pre-oder traversal.
# When we encounter a non-null node, we record the node's value.
# If it is a null node, we record using a sentinel value such as #.
#
#      _9_
#     /   \
#   3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# For example, the above binary tree can be serialized to the string
# "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
#
# Given a string of comma separated values, verify whether it is a
# correct preorder traversal serialization of a binary tree.
# Find an algorithm without reconstructing the tree.
#
# Each comma separated value in the string must be either an integer
# or a character '#' representing null pointer.
#
# You may assume that the input format is always valid, for example
# it could never contain two consecutive commas such as "1,,3".
#
# Example 1:
# "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Return true
#
# Example 2:
# "1,#"
# Return false
#
# Example 3:
# "9,#,#,1"
# Return false

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        arr, d = preorder.split(','), 0
        for i in xrange(len(arr) - 1):
            if arr[i] == '#':
                if d == 0:
                    return False
                d -= 1
            else:
                d += 1
        return True if d == 0 and arr[-1] == '#' else False


if __name__ == '__main__':
    print Solution().isValidSerialization("#,7,6,9,#,#,#")
    print Solution().isValidSerialization("7,2,#,2,#,#,#,6,#")
