# Given a list of strings, you could concatenate these strings together into a loop, where for each string you could
# choose to reverse it or not. Among all the possible loops, you need to find the lexicographically biggest string
# after cutting the loop, which will make the looped string into a regular one.
#
# Specifically, to find the lexicographically biggest string, you need to experience two phases:
#
# Concatenate all the strings into a loop, where you can reverse some strings or not and connect them in the same
# order as given.
# Cut and make one breakpoint in any place of the loop, which will make the looped string into a regular one starting
#  from the character at the cutpoint.
# And your job is to find the lexicographically biggest one among all the possible regular strings.
#
# Example:
# Input: "abc", "xyz"
# Output: "zyxcba"
# Explanation: You can get the looped string "-abcxyz-", "-abczyx-", "-cbaxyz-", "-cbazyx-",
# where '-' represents the looped status.
# The answer string came from the fourth looped one,
# where you could cut from the middle character 'a' and get "zyxcba".
# Note:
# The input strings will only contain lowercase letters.
# The total length of all the strings will not over 1,000.


class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        s, res, cur = "", "a", 0
        for str in strs:
            s += max(str, str[::-1])

        for i in xrange(len(strs)):
            tr1, tr2 = strs[i], strs[i][::-1]
            mid = s[cur + len(tr1):] + s[0:cur]  # bugfixed forget to put `:`
            for j in xrange(len(tr1)):
                if tr1[j] >= res[0]:
                    res = max(res, tr1[j:] + mid + tr1[:j])
                if tr2[j] >= res[0]:
                    res = max(res, tr2[j:] + mid + tr2[:j])  # bugfixed
            cur += len(tr1)

        return res

    def splitLoopedString2(self, strs):  # review
        """
        :type strs: List[str]
        :rtype: str
        """
        max_letter = ""
        reverse = []
        for string in strs:
            reverse.append(max(string, string[::-1]))
            max_letter = max(max_letter, max(string))  # knowledge `max(string)` to find the max char in a string

        max_string = ""
        for idx1, entry in enumerate(reverse):
            if max_letter not in entry:
                continue
            else:
                for data in (entry, entry[::-1]):  # notice ,how to generate a list and loop it
                    for idx2, l in enumerate(data):
                        if l == max_letter:
                            new_string = data[idx2:] + "".join(reverse[idx1 + 1:]) + "".join(reverse[:idx1]) + data[
                                                                                                               :idx2]
                            max_string = max(new_string, max_string)

        return max_string


if __name__ == '__main__':
    print Solution().splitLoopedString(["lc", "love", "ydc"])
    print Solution().splitLoopedString(["abc", "xyz"])
