# Time:  O(n)
# Space: O(n)

# Given a non-empty string check if it can be constructed by taking a substring of it
# and appending multiple copies of the substring together.
# You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
#
# Example 1:
# Input: "abab"
#
# Output: True
#
# Explanation: It's the substring "ab" twice.
# Example 2:
# Input: "aba"
#
# Output: False
# Example 3:
# Input: "abcabcabcabc"
#
# Output: True
#
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

# KMP solution.


class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """

        if not str:
            return False

        ss = (str + str)[1:-1]
        print ss
        return ss.find(str) != -1


if __name__ == "__main__":
    Solution().repeatedSubstringPattern("abcabc");