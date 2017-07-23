# Time:  O(t! / (n1! * n2! * ... nk!)), t is the total number of tickets,
#                                       ni is the number of the ticket which from is city i,
#                                       k is the total number of cities.
# Space: O(t)

# Given a list of airline tickets represented by pairs of departure
# and arrival airports [from, to], reconstruct the itinerary in order.
# All of the tickets belong to a man who departs from JFK.
# Thus, the itinerary must begin with JFK.
#
# Note:
# If there are multiple valid itineraries, you should return the itinerary
# that has the smallest lexical order when read as a single string.
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical
# order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets may form at least one valid itinerary.
# Example 1:
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
# Example 2:
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
# Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
# But it is larger in lexical order.

import collections


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)

        visit("JFK")
        return route[::-1]

    # review itneray solution
    def findItinerary2(self, tickets):
        target = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            target[a] += b,

        res, stack = [], ['JFK']
        while stack:
            while target[stack[-1]]:
                stack += target[stack[-1]].pop(),

            res += stack.pop(),
        return res[::-1]

        res, stack = [], ['JFK']



if __name__ == '__main__':
    print Solution().findItinerary2([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])
