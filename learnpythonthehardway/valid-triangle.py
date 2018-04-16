# Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the
# array that can make triangles if we take them as side lengths of a triangle.
# Example 1:
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Note:
# The length of the given array won't exceed 1000.
# The integers in the given array are in the range of [0, 1000].


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for l1 in xrange(len(nums)-2):
            for l2 in xrange(l1+1,len(nums)-1):
                for l3 in reversed(xrange(l2+1,len(nums))):
                    if nums[l1] + nums[l2] > nums[l3] :
                        res += l3 - l2
                        break

        return res

    def triangleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for l1 in xrange(len(nums)-2):
            for l2 in xrange(l1+1,len(nums)-1):
                s, left, right = nums[l1] + nums[l2], l2+1, len(nums)
                while left < right:
                    mid = left + (right-left) / 2
                    if nums[mid] < s:
                        left = mid + 1
                    else:
                        right = mid

                res += right - l2 - 1


        return res

if __name__ == '__main__':
    print Solution().triangleNumber([2,2,3,4])
    print Solution().triangleNumber([1,2,3,4,5,6])

