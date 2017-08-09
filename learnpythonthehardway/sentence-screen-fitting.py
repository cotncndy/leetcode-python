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

    def wordsTyping2(self, sentence, rows, cols):  # todo, try to understand
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = " " + " ".join(sentence)
        start = 0
        l = len(s)
        res = 0

        i = 1
        for _ in range(rows):
            i += cols
            if i > l - 1:
                res += i / l
                i = i % l
            # 此刻i是剩余的格数，如果i不等于“ ”就要回退i到空格处
            while s[i] != ' ':
                i -= 1

            i += 1

        return res

    def wordsTyping3(self, sentence, rows, cols):  # todo , try to understand
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = [len(w) for w in sentence]
        sentence_len = sum(s) + len(s) - 1
        times_per_row = (cols + 1) / (sentence_len + 1)
        times = times_per_row * rows
        rest_per_row = cols - times_per_row * (sentence_len + 1)

        rest_num_w = []
        for start in range(len(s)):
            rest = rest_per_row
            end = start
            num = 0
            while rest >= s[end]:
                rest -= (s[end] + 1)
                end = (end + 1) % len(s)
                num += 1
            rest_num_w.append(num)

        word_point = 0
        for _ in range(rows):
            word_point += rest_num_w[word_point]
            if word_point >= len(s):
                times += 1
            word_point = word_point % len(s)
        return times
