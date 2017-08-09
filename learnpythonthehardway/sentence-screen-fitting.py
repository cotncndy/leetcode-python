# Time:  O(r + n * c)
# Space: O(n)

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """

        def word_fit(start, cols):
            if len(sentence[start]) > cols:  # if single word is longer than whole row, we can not place it
                return 0

            s, count = len(
                sentence[start]), 1  # s is the ending pos for sen[start] word, since we placed 1 word, count=1
            i = (start + 1) % len(sentence)  # i is the next word of start, if start == 1, i = 2, or start==2, then i==0
            while s + 1 + len(sentence[i]) <= cols:  # for test case ["a", "bcd", "e"]
                s += 1 + len(sentence[i])  # new ending position for next word
                count += 1  # we could place one more word
                i = (i + 1) % len(sentence)  # go to next word
            return count

        word_row_count = [0] * len(sentence)  # how many word can each row place
        for i in xrange(len(sentence)):
            word_row_count[i] = word_fit(i, cols)

        words, start = 0, 0
        for i in xrange(rows):
            words += word_row_count[start]
            start = (start + word_row_count[start]) % len(sentence)

        return words / len(sentence)
