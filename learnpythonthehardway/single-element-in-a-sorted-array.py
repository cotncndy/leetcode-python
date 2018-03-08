# Given a sorted array consisting of only integers where every element appears twice except for one element which
# appears once. Find this single element that appears only once.
#
# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
# Note: Your solution should run in O(log n) time and O(1) space.

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if nums[mid] == nums[mid - 1]:
                if right - left == 2:
                    return nums[right]
                if mid & 1:
                    left = mid + 1
                else:
                    right = mid - 2
            else:
                if right - left == 2:
                    return nums[left]
                if mid & 1:
                    right = mid - 1
                else:
                    left = mid + 2
        return -1


if __name__ == '__main__':
    print Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])
    print Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])
    print Solution().singleNonDuplicate([1, 2, 2])
    print Solution().singleNonDuplicate([1, 1, 2])
