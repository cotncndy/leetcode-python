# Time:  O(n)
# Space: O(n)
#
# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
#

import operator


class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candies = [1] * len(ratings)
        for i in xrange(len(candies) - 1):
            if ratings[i + 1] > ratings[i]:
                candies[i + 1] = 1 + candies[i]

        for i in reversed(xrange(1, len(candies))):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i] + 1, candies[i - 1])

        return sum(candies)
