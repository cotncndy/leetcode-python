import collections


class Solution(object):
    def threeSum(self, nums):
        """

        :param nums: List[int]
        :return: List[List[int]]
        """

        nums, result, i = sorted(nums), [], 0

        while (i < len(nums) - 2):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1

            i += 1
        return result

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # d = {-1:2, 0:1, 2:1, -4:1, 1:1}
        d = collections.Counter(nums)
        # nums_2 = {-1}
        nums_2 = [x[0] for x in d.items() if x[1] > 1]
        # nums_new = {-4,-1,0,1,2}
        nums_new = sorted([x[0] for x in d.items()])
        rtn = [[0, 0, 0]] if d[0] >= 3 else []
        for i, j in enumerate(nums_new):
            if j <= 0:  # j : -1
                numss2 = nums_new[i + 1:]  # [0,1,2]
                for x, y in enumerate(numss2):  # y = 2
                    if 0 - j - y in [j, y] and 0 - j - y in nums_2:
                        if sorted([j, y, 0 - j - y]) not in rtn:
                            rtn.append(sorted([j, y, 0 - j - y]))
                    if 0 - j - y not in [j, y] and 0 - j - y in nums_new:
                        if sorted([j, y, 0 - j - y]) not in rtn:
                            rtn.append(sorted([j, y, 0 - j - y]))
        return rtn


if __name__ == "__main__":
    result = Solution().threeSum2([-1, 0, 1, 2, -1, -4])
    print result
