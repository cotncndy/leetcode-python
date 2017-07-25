# Time:  O(n * 4^n)
# Space: O(n)
#
# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
# lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.
#

# Iterative Solution
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if not digits:
            return []
        lookup, result = ["", "", "abc", "def", "ghi", "jkl", "mno", \
                          "pqrs", "tuv", "wxyz"], []

        self.dfs(result, digits, lookup, '', 0)
        return result

    def dfs(self, result, digits, lookup, temp, level):
        if level == len(digits):
            result += temp,
            return result

        for c in lookup[int(digits[level])]:
            self.dfs(result, digits, lookup, temp + c, level + 1)
