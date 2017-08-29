# Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the
# substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair
#  of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
#
# Example 1:
# Input:
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
# Example 2:
# Input:
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
# Note:
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000].


class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        if not len(dict):
            return s
        start, end, intervals = 0, 0, [];

        def merge(intervals):
            if len(intervals) < 2:
                return intervals

            merged = []

            start, end = intervals[0][0], intervals[0][1]
            for i in intervals:
                if end >= i[0]:  # if there is overlap
                    end = max(end, i[1])
                else:
                    merged.append([start, end]);
                    start, end = i[0], i[1]

            merged.append([start, end])
            return merged

        for w in dict:
            start = 0  # bugfixed
            while s.find(w, start) > -1:  # bugfixed, start's position need to be updated
                start = s.find(w, start)
                intervals.append([start, start + len(w)])
                start += 1

        sorted(intervals)
        merged = merge(intervals);
        res, prev = "", 0
        for i in merged:
            res += (s[prev:i[0]])
            res += "<b>"
            res += (s[i[0]: i[1]])
            res += ("</b>")
            prev = i[1]
        if prev < len(s):
            res += (s[prev:])

        return res


if __name__ == '__main__':
    # print Solution().addBoldTag("aaabbcc", ["aab", "abb", "bc"])
    # print Solution().addBoldTag("aaabbcc", ["d"])
# print Solution().addBoldTag("aaabbcc", [])
# print Solution().addBoldTag("abcxyz123", ["abc","123"])
    print Solution().addBoldTag("aaabbcc", ["aaa", "aab", "bc", "aaabbcc"])
