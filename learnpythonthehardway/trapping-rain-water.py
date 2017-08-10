# Time:  O(n)
# Space: O(1)
#
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
#  compute how much water it is able to trap after raining.
#
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.
#

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        l, r, res = 0, len(A), 0
        while l < r:
            min_h = min(A[l], A[r])
            if min_h == A[l]:
                l += 1
                while l < r and A[l] < min_h:
                    res += min_h - A[l]
                    l += 1
            else:
                r -= 1
                while l < r and A[r] < min_h:
                    res += min_h - A[r]
                    r -= 1

        return res
