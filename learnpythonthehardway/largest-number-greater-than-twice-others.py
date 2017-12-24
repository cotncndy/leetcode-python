class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        min1, min2, idx, res = -1, -1, 0, -1

        for i in nums:
            if min1 < i:
                min2 = min1
                min1 = i
                res = idx
            elif min2 < i:
                min2 = i
            idx += 1

        if int(min1 / min2) >= 2:
            return res
        return -1


if __name__ == '__main__':
    print Solution().dominantIndex([3, 6, 1, 0])
    print Solution().dominantIndex([1, 2, 3, 4])
