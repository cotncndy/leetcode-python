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
    def kEmptySlots_wrong(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n, m = len(flowers),{flowers[key] : key + 1 for key in xrange(len(flowers))}
        if n <= k :
            return -1

        start = n - k

        while start > 1:
            lMin, lMax = min(flowers[start:start+k:]), max(flowers[start: start+k])
            if lMin-1 not in m or lMax + 1 not in m:
                start -= 1
                continue
            minL, maxL = m[lMin-1],m[lMax+1]
            if minL < start + 2 and maxL < start + 2 and abs(lMax - lMin + 2)==k+1:
                return max(minL, maxL)
            while lMin < flowers[start + k-1] < lMax:  #bugfixed
                start -= 1
            else:
                start -= 1

        return -1

    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """

        n, m = len(flowers),{flowers[key] : key for key in xrange(len(flowers))}
        res = n+1

        for i in xrange(1, n-k):
            minP, maxP = min(m[i], m[i+k+1]), max(m[i], m[i+k+1])
            if maxP >= n-k:  # on the right, there is less than k flowers
                continue
            for t in xrange(i+1, i+k+1):
                if m[t] < maxP:
                    break
            else:
                res = min(res,maxP + 1)

        return res if res < n + 1 else -1

if __name__ == '__main__':
    # print Solution().kEmptySlots([1,5,6,2,3,4], 3)
    print Solution().kEmptySlots([1,4,6,2,3,5], 3)
    print Solution().kEmptySlots([1,3,2], 1)
    # print Solution().kEmptySlots([1,5,2,3,4,6], 3)
    # print Solution().kEmptySlots([9,1,4,2,8,7,5,3,6,10],3)
    # print Solution().kEmptySlots([1,5,2,3,4],3)
    print Solution().kEmptySlots([3,9,2,8,1,6,10,5,4,7],1)
    print Solution().kEmptySlots([6,5,8,9,7,1,10,2,3,4],2)


