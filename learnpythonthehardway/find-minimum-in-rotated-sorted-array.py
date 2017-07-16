# Time:  O(logn)
# Space: O(1)
#
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        if nums[left] > nums[right]:  # there is rotation
            while left != right - 1:  # review when left and right is adjacent, then stop the loop
                mid = left + (right - left) / 2
                if nums[mid] > nums[left]:
                    left = mid
                else:
                    right = mid

            return min(nums[left], nums[right])
        return nums[0]


if __name__ == '__main__':
    print Solution().findMin([4, 5, 6, 7, 0, 1, 2])
