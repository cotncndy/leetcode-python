class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        if not word:
            return [""]

        res, l = [], len(word)
        res.append(word)

        for i in xrange(1, 1<<l) :
            j, zero, k = i, 0, 0
            tempStr = ""
            while k < l:
                if j & 1 == 0 :
                    if zero > 0 :
                       tempStr += str(zero)
                       zero = 0
                    tempStr += word[k]
                else :
                    zero += 1

                j >>= 1
                k += 1

            if zero > 0:
                tempStr += str(zero)

            res.append(tempStr)

        return res


if __name__ == "__main__":
    strlist = Solution().generateAbbreviations("word")
    print strlist





