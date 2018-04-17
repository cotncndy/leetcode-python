# You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number
# from each of the k lists.
#
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.
#
# Example 1:
# Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# Note:
# The given list may contain duplicates, so ascending order means >= here.
# 1 <= k <= 3500
# -105 <= value of elements <= 105.
# For Java users, please note that the input type has been changed to List<List<Integer>>. And after you reset the
# code template, you'll see this point.
import collections
from _heapq import heappush


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        def hasMore() :
            for i in xrange(len(idx)):
                if idx[i] < len(nums[i]):
                    return True
            return False

        size, minHeap, maxHeap = len(nums), [], []
        idx, res = [0] * size, [float('-inf'), float('inf')]

        while hasMore():
            for k, v in enumerate(nums):
                if idx[k] >= len(v):
                    continue
                if len(minHeap) < size:
                    heappush(minHeap, v[idx[k]])
                    heappush(maxHeap, -v[idx[k]])
                    idx[k] += 1
                else:
                    if -maxHeap[0] - minHeap[0] < res[1] - res[0]:
                        res = [minHeap[0], -maxHeap[0]]
                    elif -maxHeap[0] - minHeap[0] == res[1] - res[0]:
                        if res[0] > minHeap[0]:
                            res = [minHeap[0], -maxHeap[0]]

                    minHeap.remove(v[idx[k]-1]) # bugfixed
                    maxHeap.remove(-v[idx[k]-1])
                    heappush(minHeap, v[idx[k]])
                    heappush(maxHeap, -v[idx[k]])
                    idx[k] += 1

        if -maxHeap[0] - minHeap[0] < res[1] - res[0] or (-maxHeap[0] - minHeap[0] < res[1] - res[0]  and minHeap[0] < res[0]):
            res = [minHeap[0], -maxHeap[0]]

        return res

    def smallestRange2(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        res = []
        def mergeArray(arr, i):
            l1, l2, temp = 0, 0, []
            while l1 < len(res) and l2 < len(arr):
                if res[l1][0] < arr[l2]:
                    temp.append((res[l1]))
                    l1 += 1
                else:
                    temp.append((arr[l2], i))
                    l2 += 1
            if l1 < len(res):
                for j in res[l1:]:
                    temp.append(j)
            else:
                for j in arr[l2:]:
                    temp.append((j,i))

            return temp

        for k,v in enumerate(nums):
            res = mergeArray(v,k)

        cnt , dict, left, right, n, ans = 0, collections.defaultdict(int), 0, 0, len(nums),  []
        while right < len(res):
            dict[res[right][1]] += 1
            while len(dict) == n :
                t = res[right][0] - res[left][0]
                l = float('inf') if not ans else ans[1] - ans[0]
                if l > t or (l == t and ans[0] >= left):
                    ans = [res[left][0], res[right][0]]
                left += 1
                dict[res[left][1]] -= 1
                if dict[res[left][1]] == 0:
                    del dict[res[left][1]]

            right += 1

        return ans










        print res

if __name__ == '__main__':
    # print Solution().smallestRange2([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])
    # print Solution().smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])
    # print Solution().smallestRange([[10],[11]])
    # print Solution().smallestRange2([[10],[11]])
    # print Solution().smallestRange([[1,2,3],[1,2,3],[1,2,3]])
    # print Solution().smallestRange2([[1,2,3],[1,2,3],[1,2,3]])
    # print Solution().smallestRange([[-5,-4,-3,-2,-1],[1,2,3,4,5]])
    print Solution().smallestRange2([[-5,-4,-3,-2,-1],[1,2,3,4,5]])





