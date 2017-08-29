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

        intervals = sorted(
            intervals)  # bugfixed, alternative, should use a = sorted(a), I confused it with java sort(a)
        # intervals.sort(key=lambda x: x[0])  # bugfixed, need to sort by key
        merged = merge(intervals)
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

    def addBoldTag2(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """

        # find all overlapping matches
        def merge(interval):
            res = []
            for i in interval:
                if res and i[0] <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], i[1])
                else:
                    res.append(i)
            return res

        matches = []
        for word in dict:
            start = 0
            while True:
                start = s.find(word, start)
                if start == -1:
                    break
                else:
                    matches.append([start, start + len(word)])
                    start += 1
        # merge all matches like intervals
        matches = sorted(matches)
        # self.mergeInterval(matches)
        matches = merge(matches)
        # concatenate string
        ret = ""
        pos = 0
        for start, end in matches:
            ret += s[pos:start] + '<b>' + s[start:end] + '</b>'
            pos = end
        ret += s[pos:]
        return ret


if __name__ == '__main__':
    # print Solution().addBoldTag("aaabbcc", ["aab", "abb", "bc"])
    # print Solution().addBoldTag("aaabbcc", ["d"])
    # print Solution().addBoldTag("aaabbcc", [])
    # print Solution().addBoldTag("abcxyz123", ["abc","123"])
    print Solution().addBoldTag(
        "xhhjzbkvpmasiypsqqjobufcqmlhdjffrdohsxgksftaekzhwzydhbfdiylihnvjlvpoptnqigszckimljbepgisnmyszfsxkxyfdfqngytfuihepohapvhbyhqydvroflfnsyjmygtykdejfudrhxxawcewgiguiwsvqrgbxrbdnrvguzjftqcsjbvjlbxfsvzpdpmtlzobwnxrtgisbcqmhugncjwgatfctydryakvbnmlbiftndfefylsmlebzdumefuflwhtwijtrhhhmknklalgqjaoicmnywtvzldbeftkydjsdkkonayhdxhrjazosqloilagcwzeezavnsqelxqhtlzymedxmkrovxhkrgfenyhxgdroeejedbwpnkqbqknalwgxoxweyxngorvrpnfkvagdqkbtuayaihyhwcsdtjzzvxfavrhzgf",
        [
            "xh", "hj", "zb", "kv", "pm", "as", "iy", "ps", "qq", "jo", "bu", "fc", "qm", "lh", "dj", "ff", "rd",
            "oh", "sx", "gk", "sf", "ta", "ek", "zh", "wz", "yd", "hb", "fd", "li", "hn", "vj", "lv", "po", "pt", "nq",
            "ig", "sz", "ck", "im", "lj", "be", "pg", "is", "nm", "ys", "zf", "kx"])
