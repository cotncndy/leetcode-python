# Time:  O(n)
# Space: O(k), k is maxWidth.
#
# Given an array of words and a length L, format the text such that
# each line has exactly L characters and is fully (left and right) justified.
#
# You should pack your words in a greedy approach; that is, pack
# as many words as you can in each line. Pad extra spaces ' '
# when necessary so that each line has exactly L characters.
#
# Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line do not divide evenly between words,
# the empty slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space
# is inserted between words.
#
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
#
# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Note: Each word is guaranteed not to exceed L in length.

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        i, s = 0, []
        while i < len(words):
            leng, j, line = 0, i, ""
            while j < len(words) and leng + len(words[j]) + j - i <= maxWidth:
                leng += len(words[j])
                j += 1

            space = maxWidth - leng
            for k in xrange(i, j):
                line += words[k]
                if space > 0:
                    temp = 0
                    if j == len(words):  ## arive the last word, so it is the last line
                        if j - k == 1:  ## last line has only one word
                            temp = space
                        else:
                            temp = 1  # has more than one word
                    else:
                        if j - k - 1 > 0:  # not the last line and has more than one word
                            if space % (j - k - 1) == 0:
                                temp = space / (j - k - 1)
                            else:  ## put one more space on the left
                                temp = space / (j - k - 1) + 1
                        else:  ## if just have one word, then use all spaces
                            temp = space

                    line += ' ' * temp
                    space -= temp

            s += line
            i = j

        return s


if __name__ == "__main__":
    print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
