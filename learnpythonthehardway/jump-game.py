# Time:  O(n)
# Space: O(1)
#
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# For example:
# A = [2,3,1,1,4], return true.
#
# A = [3,2,1,0,4], return false.

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        max_reach = 0
        for i, e in enumerate(A):
            if i > max_reach:
                break
            max_reach = max(max_reach, i + e)

        return max_reach >= (len(A) - 1)
