#  Given a word, you need to judge whether the usage of capitals in it is right or not.
#
# We define the usage of capitals in a word to be right when one of the following cases holds:
#
#     All letters in this word are capitals, like "USA".
#     All letters in this word are not capitals, like "leetcode".
#     Only the first letter in this word is capital if it has more than one letter, like "Google".
#
# Otherwise, we define that this word doesn't use capitals in a right way.
#
# Example 1:
#
# Input: "USA"
# Output: True
#
# Example 2:
#
# Input: "FlaG"
# Output: False
#
# Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cnt = 0
        for c in word:
            if c.isupper():
                cnt += 1

        return cnt == 0 or cnt == len(word) or (cnt == 1 and word[0].isupper())

    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()

if __name__ == '__main__':
    print Solution().detectCapitalUse("Hello")
    print Solution().detectCapitalUse("USA")
    print Solution().detectCapitalUse("googlE")
    print Solution().detectCapitalUse("Google")
    print Solution().detectCapitalUse("gooGle")
