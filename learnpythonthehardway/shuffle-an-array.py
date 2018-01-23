# Shuffle a set of numbers without duplicates.
#
# Example:
#
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
#
# // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();
#
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
#
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._arr = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self._arr

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        temp = []
        temp.extend(self._arr)  # bugfixed notice copy by-value vs copy by-reference
        for i in reversed(xrange(len(temp))):
            j = random.randint(0, i)
            temp[i], temp[j] = temp[j], temp[i]

        return temp

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
