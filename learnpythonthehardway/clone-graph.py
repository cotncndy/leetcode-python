# Time:  O(n)
# Space: O(n)
#
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
#
#
# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
#
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
#
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
#
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:
#
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/
#
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        cloned_node = UndirectedGraphNode(node.label)
        clones, queue = {node: cloned_node}, [node]

        while queue:
            curr = queue.pop()
            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    copy = UndirectedGraphNode(neighbor.label)
                    clones[neighbor] = copy
                    queue.append(neighbor)
                clones[curr].neighbors.append(clones[neighbor])

        return cloned_node

    def cloneGraph2(self, node):
        lookup = {}
        return self.dfs(node, lookup)

    def dfs(self, node, lookup):
        if not node:
            return node
        if node in lookup:
            return lookup[node]
        clone = UndirectedGraphNode(node.label)
        lookup[node] = clone
        for n in node.neighbors:
            clone.neighbors.append(self.dfs(n, lookup))

        return clone
