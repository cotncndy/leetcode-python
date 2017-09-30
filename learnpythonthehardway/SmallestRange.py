# You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number
# from each of the k lists.
#
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.
#
# Example 1:
# Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# Note:
# The given list may contain duplicates, so ascending order means >= here.
# 1 <= k <= 3500
# -105 <= value of elements <= 105.
# For Java users, please note that the input type has been changed to List<List<Integer>>. And after you reset the
# code template, you'll see this point.


from heapq import heappop, heappush
import bisect


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        min_heap, max_heap = [], []

        for i in xrange(len(nums)):
            for j in xrange(len(nums[i])):
                heappush(min_heap, (nums[i][j], i, j))
                heappush(max_heap, (-nums[i][j], i, j))

        left, right = -1, -1
        while min_heap:  # for smallest range, we want to minizie (right-left), so we keey push left to the right
            left, i, j = heappop(min_heap)  # for ex, for test case [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
            if j == len(nums[i]) - 1:  # the rightmost left is 20
                break;

        while max_heap:
            val, i, j = heappop(max_heap)  # get the biggest right
            valid = True
            if j >= 0 and -val >= left:
                for x in xrange(len(nums)):
                    if x == i: continue
                    k = bisect.bisect_left(nums[x], -val)  # binary search, for right, we need it exists in every array
                    if nums[x][k - 1] < left:  # right can not be less then left
                        valid = False
                        break;
                if valid:
                    right = -val
                    continue
            else:
                break;
        return [left, right]


if __name__ == '__main__':
    # for this test case, my algorithm can get correct answer [20, 24]
    print Solution().smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
    # but for this one, I got wrong ans, [3,4], but it should be [1,2], smallest range not only has min(right-left),
    # when we have same (right-left), we want min left.
    print Solution().smallestRange([[1, 2, 3], [1, 2, 4]])
