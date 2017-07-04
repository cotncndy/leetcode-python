class Solution:
    # @return an integer
    def romanToInt(self, s):
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i in xrange(len(s)):
            if i == len(s) - 1 or numeral_map[s[i + 1]] <= numeral_map[s[i]]:
                res += numeral_map[s[i]]
            else:
                res -= numeral_map[s[i]]

        return res


if __name__ == '__main__':
    print Solution().romanToInt("DCXXI")
