# Time:  O(n)
# Space: O(1)
#
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.
#
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        longest, left, table = 0, 0, [0 for _ in xrange(256)]
        for i, ch in enumerate(s):
            if table[ord(ch)] == 0 or table[ord(ch)] < left:
                longest = max(longest, i - left + 1)
            else:
                left = table[ord(ch)]

            table[ord(ch)] = i + 1

        return longest

    # use set to do it, even easier
    def lengthOfLongestSubstring2(self, s):
        res, left, right, tset = 0, 0, 0, set()  # review how to use set https://en.wikibooks.org/wiki/Python_Programming/Sets
        for c in s:
            if not c in tset:
                tset.add(c)
                res = max(res, len(tset))
            else:
                while c in tset:
                    tset.remove(s[left])
                    left += 1
                # after remove all the way to the duplicate one
                # you need also add it
                tset.add(c)

        return res


if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring2("abcabcbb")
