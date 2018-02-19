# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
#
# You need to return the number of important reverse pairs in the given array.
#
# Example1:
#
# Input: [1,3,2,3,1]
# Output: 2
#
# Example2:
#
# Input: [2,4,3,5,1]
# Output: 3
#
# Note:
#
#     The length of the given array will not exceed 50,000.
#     All the numbers in the input array are in the range of 32-bit integer.


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def merge_sort(nums, start, end):
            if start >= end:
                return 0
            mid, count = start + (end - start) / 2, 0
            count = merge_sort(nums, start, mid) + merge_sort(nums, mid + 1, end)

            r, temp = mid + 1, []
            j = 0

            for i in xrange(start, mid + 1):
                while r <= end and nums[r] * 2 < nums[i]:
                    r += 1

                count += r - (mid + 1)

            r = mid + 1
            for i in xrange(start, mid + 1):  # merge it
                while r <= end and nums[r] < nums[i]:
                    temp.append(nums[r])
                    r += 1
                temp.append(nums[i])
            nums[start: start + len(temp)] = temp
            return count

        return merge_sort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    print Solution().reversePairs([1, 3, 2, 3, 1])
    print Solution().reversePairs([2, 4, 3, 5, 1])
