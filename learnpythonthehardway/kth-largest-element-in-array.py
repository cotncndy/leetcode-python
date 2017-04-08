# Time:  O(n) ~ O(n^2)
# Space: O(1)
from random import randint

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        left, right = 0, len(nums)-1;
        while left <= right:
            pivot_idx = randint(left,right)
            part = self.partition(left,right,pivot_idx,nums);
            if part == k-1:
                return nums[part]
            elif part > k-1:
                right = part-1
            else:
                left = part+1


    def partition(self, left, right, pivot, nums):
        pivot_value = nums[pivot]
        k = left
        nums[pivot], nums[right] = nums[right], nums[pivot]
        for i in xrange(left,right):
            if nums[i] > pivot_value:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1

        nums[right], nums[k] = nums[k], nums[right]
        return k


if __name__ == "__main__":
    nums = [7,3,1,2,9,4,6,5,8]
    print Solution().findKthLargest(nums,2)




