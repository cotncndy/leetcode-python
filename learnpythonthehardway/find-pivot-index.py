class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        sum = [0] * len(nums)
        for k, v in enumerate(nums):
            if k == 0:
                sum[k] = v
            else:
                sum[k] = sum[k - 1] + v

        for i in xrange(0, len(sum)):
            if i > 0 and sum[-1] - sum[i] == sum[i - 1]:
                return i
            elif i == 0 and sum[-1] - sum[i] == 0:
                return i
            elif i == len(sum) - 1 and sum[i - 1] == 0:
                return i
        return -1


if __name__ == '__main__':
    # print Solution().pivotIndex([1,7,3,6,5,6])
    # print Solution().pivotIndex([1,2,3])
    print Solution().pivotIndex([1, 2])
    print Solution().pivotIndex([1])
    print Solution().pivotIndex([-1, -1, -1, 0, 1, 1])
    print Solution().pivotIndex([-1, 0, 1, 0])
