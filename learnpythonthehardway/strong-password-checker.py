# A password is considered strong if below conditions are all met:
#
# It has at least 6 characters and at most 20 characters.
# It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
# It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong,
# assuming other conditions are met).
# Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required
# to make s a strong password. If s is already strong, return 0.
#
# Insertion, deletion or replace of any one character are all considered as one change.


class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        missingType, res = 3, 0
        if any('a' <= c <= 'z' for c in s):
            missingType -= 1
        if any('A' <= c <= 'Z' for c in s):
            missingType -= 1
        if any(c.isdigit() for c in s):
            missingType -= 1

        if len(s) < 6:
            return max(missingType, 6 - len(s))
        delete = 0
        if len(s) > 20:
            delete = len(s) - 20
        start, change = 0, 0
        while start < len(s) - 2:
            if s[start] == s[start + 1] and s[start + 1] == s[start + 2]:
                change += 1
                start += 3
            else:
                start += 1

        # now I have delete and change, missing type
        if delete >= change:
            delete -= change  # delete the consecutive letters
            res += delete
        else:
            change -= delete  # delete the consective letters






        res += max(missingType, change)

        return res

    def strongPasswordChecker2(self, s):
        """
        :type s: str
        :rtype: int
        """
        missing_type = 3
        if any('a' <= c <= 'z' for c in s): missing_type -= 1
        if any('A' <= c <= 'Z' for c in s): missing_type -= 1
        if any(c.isdigit() for c in s): missing_type -= 1

        change = 0
        one = two = 0
        p = 2
        while p < len(s):
            if s[p] == s[p - 1] == s[p - 2]:
                length = 2
                while p < len(s) and s[p] == s[p - 1]:
                    length += 1
                    p += 1

                change += length / 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            else:
                p += 1

        if len(s) < 6:
            return max(missing_type, 6 - len(s))
        elif len(s) <= 20:
            return max(missing_type, change)
        else:
            delete = len(s) - 20

            change -= min(delete, one)
            change -= min(max(delete - one, 0), two * 2) / 2
            change -= max(delete - one - 2 * two, 0) / 3

            return delete + max(missing_type, change)


if __name__ == '__main__':
    print Solution().strongPasswordChecker2("abc")
    print Solution().strongPasswordChecker("abc")
    print Solution().strongPasswordChecker("aaa")
    print Solution().strongPasswordChecker2("aaa")
    print Solution().strongPasswordChecker("@#!$")
    print Solution().strongPasswordChecker2("@#!$")
    print Solution().strongPasswordChecker("@#!$$$$$$$$$$$$$$$$$$$$$$$")
    print Solution().strongPasswordChecker2("@#!$$$$$$$$$$$$$$$$$$$$$$$")
    print Solution().strongPasswordChecker("12345678910111213141516")
    print Solution().strongPasswordChecker2("12345678910111213141516")
    print Solution().strongPasswordChecker("AaAbbbcc")
    print Solution().strongPasswordChecker2("AaAbbbcc")
    print Solution().strongPasswordChecker("aaa111")
    print Solution().strongPasswordChecker2("aaa111")
    print Solution().strongPasswordChecker("1010101010aaaB10101010")
    print Solution().strongPasswordChecker2("1010101010aaaB10101010")
