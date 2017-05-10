# Time:  O(n)
# Space: O(1)

# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.
#
# Now your job is to find the total Hamming distance between all pairs of the given numbers.
#
# Example:
# Input: 4, 14, 2
#
# Output: 6
#
# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
# showing the four bits relevant in this case). So the answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
# Note:
# Elements of the given array are in the range of 0 to 10^9
# Length of the array will not exceed 10^4.

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in xrange(32):
            k,ones = (1 << i),0
            for n in nums:
                if k & n:
                    ones += 1
            total += ones * (len(nums) - ones)
        return total

    def totalHammingDistance2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in xrange(32):
            ans = [0]*2
            for n in nums:
                ans[(n>>i) & 1] += 1
            total += ans[0] * ans[1]

        return total



if __name__ == "__main__":
    nums = [4,2,14]
    print Solution().totalHammingDistance2(nums)