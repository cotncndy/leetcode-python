# There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In
# each day, there will be exactly one flower blooming and it will be in the status of blooming since then.
#
# Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the
# flower will open in that day.
#
# For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x
# will be in the range from 1 to N.
#
# Also given an integer k, you need to output in which day there exists two flowers in the status of blooming,
# and also the number of flowers between them is k and these flowers are not blooming.
#
# If there isn't such day, output -1.
#
# Example 1:
# Input:
# flowers: [1,3,2]
# k: 1
# Output: 2
# Explanation: In the second day, the first and the third flower have become blooming.
# Example 2:
# Input:
# flowers: [1,2,3]
# k: 1
# Output: -1
# Note:
# The given array will be in the range [1, 20000].

class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n, m = len(flowers),{flowers[key] : key + 1 for key in xrange(len(flowers))}
        if n <= k :
            return -1

        start = n - k

        while start > 2:
            lMin, lMax = min(flowers[start:start+k:]), max(flowers[start: start+k])
            if lMin-1 not in m or lMax + 1 not in m:
                start -= 1
                continue
            minL, maxL = m[lMin-1],m[lMax+1]
            if minL < start + 2 and maxL < start + 2 and abs(lMax - lMin + 2)==k+1:
                return max(minL, maxL)
            while lMin < flowers[start + k] < lMax:
                start -= 1

        return -1
if __name__ == '__main__':
    # print Solution().kEmptySlots([1,5,6,2,3,4], 3)
    # print Solution().kEmptySlots([1,4,6,2,3,5], 3)
    # print Solution().kEmptySlots([1,3,2], 1)
    print Solution().kEmptySlots([1,5,2,3,4,6], 3)


