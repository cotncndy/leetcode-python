import collections


class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """

        if len(words1) != len(words2):
            return False
        dict = collections.defaultdict(set)
        for a, b in pairs:
            dict[a].add(b)
            dict[b].add(a)

        w1, w2 = [], []
        for i in xrange(len(words1)):
            if words1[i] != words2[i]:
                w1.append(words1[i])
                w2.append(words2[i])

        for i in xrange(len(w1)):
            if w2[i] not in dict[w1[i]]:
                return False

        return True


if __name__ == '__main__':
    print Solution().areSentencesSimilar(["great", "acting", "skills"], ["fine", "drama", "talent"],
                                         [["great", "fine"], ["drama", "acting"], ["skills", "talent"]])
    print Solution().areSentencesSimilar(["great", "acting", "skills"], ["fine", "acting", "talent"],
                                         [["great", "fine"], ["drama", "acting"], ["skills", "talent"]])

    print Solution().areSentencesSimilar(["an", "extraordinary", "meal"], ["one", "good", "dinner"],
                                         [["great", "good"], ["extraordinary", "good"], ["well", "good"],
                                          ["wonderful", "good"], ["excellent", "good"], ["fine", "good"],
                                          ["nice", "good"], ["any", "one"], ["some", "one"], ["unique", "one"],
                                          ["the", "one"], ["an", "one"], ["single", "one"], ["a", "one"],
                                          ["truck", "car"], ["wagon", "car"], ["automobile", "car"], ["auto", "car"],
                                          ["vehicle", "car"], ["entertain", "have"], ["drink", "have"], ["eat", "have"],
                                          ["take", "have"], ["fruits", "meal"], ["brunch", "meal"],
                                          ["breakfast", "meal"], ["food", "meal"], ["dinner", "meal"],
                                          ["super", "meal"], ["lunch", "meal"], ["possess", "own"], ["keep", "own"],
                                          ["have", "own"], ["extremely", "very"], ["actually", "very"],
                                          ["really", "very"], ["super", "very"]])
