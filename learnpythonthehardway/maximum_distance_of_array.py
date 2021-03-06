# Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different
# arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be
#  their absolute difference |a-b|. Your task is to find the maximum distance.
#
# Example 1:
# Input:
# [[1,2,3],
#  [4,5],
#  [1,2,3]]
# Output: 4
# Explanation:
# One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
# Note:
# Each given array will have at least 1 number. There will be at least two non-empty arrays.
# The total number of the integers in all the m arrays will be in the range of [2, 10000].
# The integers in the m arrays will be in the range of [-10000, 10000].


class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        min_a1, max_a1, res = arrays[0][0], arrays[0][-1], 0
        for i in xrange(1, len(arrays)):
            res = max(res, abs(arrays[i][0] - max_a1), abs(arrays[i][-1] - min_a1))
            min_a1, max_a1 = min(min_a1, arrays[i][0]), max(max_a1, arrays[i][-1])  # bugfixed


        return res


if __name__ == '__main__':
    print Solution().maxDistance([[-8, -7, -7, -5, 1, 1, 3, 4], [-2], [-10, -10, -7, 0, 1, 3], [2]])
