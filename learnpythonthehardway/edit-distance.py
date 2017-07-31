# Time:  O(n * m)
# Space: O(n + m)
#
# Given two words word1 and word2, find the minimum number of steps
# required to convert word1 to word2. (each operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
#
# a) Insert a character
# b) Delete a character
# c) Replace a character
#

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if len(word1) < len(word2):
            return self.minDistance(word2, word1)

        distance = [i for i in xrange(len(word2) + 1)]

        for i in xrange(len(word1) + 1):
            pre_dist_i_j = distance[0]
            distance[0] = i
            for j in xrange(len(word2) + 1):
                insert = distance[j - 1] + 1
                delete = distance[j] + 1
                repace = pre_dist_i_j
                if word1[i] != word2[j]:  # bugfixed, should be i-1 and j-1
                    repace += 1
                pre_dist_i_j = distance[j]
                distance[j] = min(insert, delete, repace)

        return distance[-1]
