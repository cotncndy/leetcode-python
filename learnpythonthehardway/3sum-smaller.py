# Time:  O(n^2)
# Space: O(1)

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumSmaller(self, nums, target):
        nums.sort()
        n = len(nums)

        count, k = 0, 2
        while k < n:
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] < target:
                    count += j - i
                    i += 1
                else:
                    j -= 1
            k += 1
        return count

    def threeSumSmaller2(self, nums, target):
        nums.sort()
        count = 0
        for i in xrange(0, len(nums) - 1):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < target:
                    count += k - j
                    j += 1
                else:
                    k -= 1
            return count
