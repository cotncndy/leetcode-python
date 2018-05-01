# Time:  O(log(min(m, n)))
# Space: O(1)

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        return (self.getkth(nums1, nums2, (m + n + 1) / 2) + self.getkth(nums1, nums2, (m + n + 2) / 2)) * 1.0 / 2

    def getkth(self, A, B, k):
        m, n = len(A), len(B)
        if m > n:
            return self.getkth(B, A, k)
        if m == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])
        i, j = min(m, k / 2), min(n, k / 2)
        if A[i - 1] > B[j - 1]:
            return self.getkth(A, B[j::], k - j)
        else:
            return self.getkth(A[i::], B, k - i)


if __name__ == '__main__':
    # print Solution().getkth([1,3,5,7,9],[2,4,6,8,10], 5)
    print Solution().getkth([1,200,203,207,209],[100,150,192,203,205], 5)
