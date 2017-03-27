# Time:  O(n)
# Space: O(n)
#
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#
# Your algorithm should run in O(n) complexity.
#

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        result, length = 1, {key: 0 for key in num}
        for i in num:
            if length[i] == 0:
                length[i] = 1
                left, right = length.get(i-1,0) , length.get(i+1,0)
                temp_len = 1 + left + right
                result, length[i-left],length[i+right] = max(result,temp_len), temp_len,temp_len
        return result

if __name__ == "__main__":
    print Solution().longestConsecutive([100, 4, 200, 1, 3, 2])