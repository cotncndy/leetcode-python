# Time:  O(n)
# Space: O(n)

# Given a non-empty array of numbers, a0, a1, a2, ... , an-1, where 0 <= ai < 231.
#
# Find the maximum result of ai XOR aj, where 0 <= i, j < n.
#
# Could you do this in O(n) runtime?
#
# Example:
#
# Input: [3, 10, 5, 25, 2, 8]
#
# Output: 28
#
# Explanation: The maximum result is 5 ^ 25 = 28.

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result,mask = 0,0
        for i in reversed(xrange(32)):
            mask |= 1 << i
            prefixes = set()
            for n in nums:
                prefixes.add(n & mask)
            t = result | (1<<i)
            for k in prefixes:
                if k ^ t in prefixes:
                    result = t
                    break

        return result

    def findMaximumXOR2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        for i in reversed(xrange(32)):
            result <<= 1
            prefixes = set()
            for n in nums:
                prefixes.add(n >> i)
            for p in prefixes:
                if (result | 1) ^ p in prefixes:
                    result += 1
                    break

        return result

if __name__ == "__main__":
    nums = [10,7,12]
    print Solution().findMaximumXOR2(nums)




