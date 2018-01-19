# Time:  O(n)
# Space: O(h), h is the depth of the recursion

# Given an encoded string, return it's decoded string.
#
# The encoding rule is: k[encoded_string],
# where the encoded_string inside the square brackets is
# being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
#
# You may assume that the input string is always valid;
# No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not
# contain any digits and that digits are only for those repeat numbers, k.
# For example, there won't be input like 3a or 2[4].
#
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack_num, stack_str, st, sr = [], [], 0, ""
        for i in xrange(len(s)):
            if s[i].isdigit():
                st = st * 10 + int(s[i])
            elif s[i] == '[':
                stack_num.append(st)
                st = 0
                stack_str.append(sr)
                sr = ""  # don't forget this which cause trouble
            elif s[i] == ']':
                cur = stack_num.pop()
                for i in xrange(cur):
                    stack_str[-1] += sr
                sr = stack_str.pop()
            else:
                sr += s[i]
        return sr

    def decodeString2(self, s):
        global x
        x = 0
        return self.decode(s)

    def decode(self, s):
        global x
        res = ""
        while x < len(s) and s[x] != ']':
            if s[x].isalpha():
                res += s[x]
                x += 1
            elif s[x].isdigit():
                cnt = 0
                while s[x].isdigit():
                    cnt = cnt * 10 + int(s[x])
                    x += 1
                x += 1  # escape `[` charcater, because `[` for sure would follow the number

                st = self.decode(s)
                x += 1
                while cnt:
                    res += st
                    cnt -= 1

        return res



if __name__ == '__main__':
    print Solution().decodeString("3[a]2[bc]")
    print Solution().decodeString2("3[a]2[2[abc]bc]]")
