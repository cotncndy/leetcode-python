# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending
# order, then the whole array will be sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack1, stack2 = [], []
        rMin, rMax = len(nums), 0
        for i in xrange(len(nums)):
            if not stack1 or nums[i] >= nums[stack1[-1]]:
                stack1.append(i)
            elif nums[i] < nums[stack1[-1]]:
                while stack1 and nums[i] < nums[stack1[-1]]:  # bugfixed empty check
                    rMax, rMin = max(rMax, i), min(rMin, stack1[-1])
                    stack2.append(stack1.pop())
                stack1.append(i)

                while stack2:
                    stack1.append(stack2.pop())

        return 0 if rMax - rMin < 0 else rMax - rMin + 1

    def findUnsortedSubarray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, start = 0, -1
        for i in xrange(1, len(nums)):
            if nums[i] < nums[i - 1]:
                j = i
                while j > 0 and nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    j -= 1

                if start == -1 or start > j:
                    start = j

                res = max(res, i - start + 1)
        return res

    def findUnsortedSubarray3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sorted(nums)

        l, m = 0, len(nums) - 1

        while l < len(nums) and a[l] == nums[l]:
            l += 1

        while m > l and a[m] == nums[m]:
            m -= 1


        return m - l + 1



if __name__ == '__main__':
    # print Solution().findUnsortedSubarray3([2, 6, 4, 8, 10, 9, 15])
    # print Solution().findUnsortedSubarray3([1, 4, 3, 5, 6, 2, 7, 8, 9])
    print Solution().findUnsortedSubarray3([2, 1])
    print Solution().findUnsortedSubarray3([1, 2, 3, 4, 5])
    print Solution().findUnsortedSubarray3([5, 4, 3, 2, 1])
