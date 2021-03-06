# Time:  O(n)
# Space: O(1)

# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if
# the ransom  note can be constructed from the magazines ;
# otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = [0] * 26

        for c in magazine:
            counts[ord(c) - ord('a')] += 1

        for c in ransomNote:
            counts[ord(c) - ord('a')] -= 1
            if counts[ord(c) - ord('a')] < 0:
                return False

        return True

    def canConstruct2(self, ransomNote, magazine):
        rset, mset = set(ransomNote), set(magazine)
        if not rset <= mset:  # bugfixed should be <= rather than <
            return False
        for c in rset:
            if ransomNote.count(c) > magazine.count(c):
                return False

        return True


if __name__ == '__main__':
    print Solution().canConstruct2("", "")
