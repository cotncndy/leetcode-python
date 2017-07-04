# Time:  O(n)
# Space: O(1)
#
# Given an integer, convert it to a roman numeral.
#
# Input is guaranteed to be within the range from 1 to 3999.
#


class Solution:
    # @return a string
    def intToRoman(self, num):
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD",
                       500: "D", 900: "CM", 1000: "M"}

        key_set, res = sorted(numeral_map.keys()), ""

        while num:
            for key in reversed(key_set):
                while num / key:
                    num -= key
                    res += numeral_map[key]

        return res
