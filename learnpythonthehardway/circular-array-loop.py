# You are given an array of positive and negative integers. If a number n at an index is positive, then move forward
# n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward
#  next to the last element, and the last element is backward next to the first element. Determine if there is a loop
#  in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must
#  be "forward" or "backward'.
#
# Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.
# Example 2: Given the array [-1, 2], there is no loop.
#
# Note: The given array is guaranteed to contain no element "0".
#
# Can you do it in O(n) time complexity and O(1) space complexity?

class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in xrange(len(nums)):
            slow, fast = i, i
            while True:  # [-1,-2, -3,-4, -5]
                s = self.goNext(nums, slow)  # 4
                if slow == s or s == self.goNext(nums, s):
                    break
                f = self.goNext(nums, self.goNext(nums, fast))  # 4

                if s == f:
                    if nums[s] * nums[slow] > 0 and nums[f] * nums[fast] > 0:
                        return True
                    return False
                fast, slow = f, s

        return False

    def goNext(self, nums, k):
        t = (k + nums[k]) % len(nums)
        return t if t >= 0 else t + len(nums)

    def circularArrayLoop2(self, nums):
        m, visited = {}, [False] * len(nums)
        for i in xrange(len(nums)):
            if visited[i]:
                continue
            visited[i] = True
            t = self.goNext(nums, i)
            while nums[i] * nums[t] > 0:
                if t == i:  # only one element
                    break  # bugfixed for ex [-1,2] if t = 1, i = 1, then infinite loop
                if t in m:
                    return True
                m[i], i, visited[t] = t, t, True  # bugfixed , need to record m[i] = t here
                t = self.goNext(nums, t)
        return False



if __name__ == '__main__':
    # print Solution().circularArrayLoop2([2, -1, 1, 2, 2])
    # print Solution().circularArrayLoop2([-1, 2])
    # print Solution().circularArrayLoop2([-2, 1, -1, -2, -2])
    print Solution().circularArrayLoop2([-1, -2, -3, -4, -5])
    print Solution().circularArrayLoop([-1, -2, -3, -4, -5])
