# Time:  O(n)
# Space: O(n)
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
import collections


class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        dict, rooling_hash, res = {}, 0, []

        for i in xrange(len(s)):
            rooling_hash = rooling_hash << 3 & 0x3fffffff | ord(s[i]) & 7
            if rooling_hash not in dict:
                dict[rooling_hash] = True
            elif dict[rooling_hash]:
                res.append(s[i - 9: i + 1])
                # critical ,if we found, mark it as False, avoid duplication results
                dict[rooling_hash] = False
        return res

    def findRepeatedDnaSequences2(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l, r = [], []
        if len(s) < 10:
            return []
        for i in range(len(s) - 9):
            l.extend([s[i:i + 10]])  # review the usage of extend

        return [k for k, v in collections.Counter(l).items() if v > 1]  # review the usage of Collections.counter



if __name__ == "__main__":
    print Solution().findRepeatedDnaSequences("AAAAAAAAAAAA")
    print Solution().findRepeatedDnaSequences("")
    print Solution().findRepeatedDnaSequences2("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
