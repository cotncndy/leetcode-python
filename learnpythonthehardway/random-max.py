# 给你一个array，返回array里面最大数字的index，但是必须是最大数字里面随机的一个index。比如[2,1,2,1,5,4,5,5]必须返回[4,6,7]中的
# 随机的一个数字，要求O(1)space。
import random


class Solution(object):
    def random_max(self, nums):
        ret, count, max_n = 0, 0, float('-inf')
        for i in xrange(len(nums)):
            if nums[i] > max_n:
                max_n, count, ret = nums[i], 1, i
            elif nums[i] == max_n:
                j = random.randint(0, count)
                count += 1
                if j == 0:
                    ret = i

        return ret


if __name__ == '__main__':
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])

    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
    print Solution().random_max([2, 1, 2, 1, 5, 4, 5, 5])
