# Time:  O(nlogn)
# Space: O(n)
#
# Given an unsorted array of integers,
# find the length of longest increasing subsequence.
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101],
# therefore the length is 4. Note that there may be more
# than one LIS combination, it is only necessary for you to return the length.
#
# Your algorithm should run in O(n2) complexity.
#
# Follow up: Could you improve it to O(n log n) time complexity?
#

# Binary search solution.
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = []

        def insert(target):
            left, right = 0, len(LIS) - 1
            while left <= right:
                mid = (left + right) / 2
                if LIS[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            if left == len(LIS):  # bugfixed left == len(LIS)-1 is wrong
                LIS.append(target)
            else:
                LIS[left] = target

        for n in nums:
            insert(n)

        return len(LIS)

    def lengthOfLIS2(self, nums):
        LIS = []

        def insert(target):
            left, right = 0, len(LIS)
            while left < right:
                mid = (left + right) / 2
                if LIS[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            if right >= len(LIS):
                LIS.append(target)
            else:
                LIS[right] = target

        for n in nums:
            insert(n)
        return len(LIS)



if __name__ == '__main__':
    print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
