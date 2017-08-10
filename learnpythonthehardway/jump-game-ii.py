# Time:  O(n)
# Space: O(1)
#
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# For example:
# Given array A = [2,3,1,1,4]
#
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#

# not pass on leetcode because of time limit
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        jump_count, last, cur = 0, 0, 0
        for i in xrange(len(A)):
            if i > last:
                last, jump_count = cur, jump_count + 1
            cur = max(cur, i + A[i])

        return jump_count


if __name__ == '__main__':
    print Solution().jump([2, 3, 1, 1, 4])
