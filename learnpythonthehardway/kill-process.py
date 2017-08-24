# Given n processes, each process has a unique PID (process id) and its PPID (parent process id).
#
# Each process only has one parent process, but may have one or more children processes. This is just like a tree
# structure. Only one process has PPID that is 0, which means this process has no parent process. All the PIDs will
# be distinct positive integers.
#
# We use two list of integers to represent a list of processes, where the first list contains PID for each process
# and the second list contains the corresponding PPID.
#
# Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that
#  will be killed in the end. You should assume that when a process is killed, all its children processes will be
# killed. No order is required for the final answer.
#
# Example 1:
# Input:
# pid =  [1, 3, 10, 5]
# ppid = [3, 0, 5, 3]
# kill = 5
# Output: [5,10]
# Explanation:
#            3
#          /   \
#         1     5
#              /
#             10
# Kill 5 will also kill 10.
# Note:
# The given kill id is guaranteed to be one of the given PIDs.
# n >= 1.
import collections


class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        map, queue, res = collections.defaultdict(list), [kill], []  # bugfixed should be defaultdit instead of
        # defaultDict
        for i in xrange(len(pid)):
            map[ppid[i]] += pid[i],

        while queue:
            child = queue.pop(0)
            res.append(child)
            if not map[child]:
                continue
            for c in map[child]:
                queue.append(c)

        return res

    def killProcess2(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """

        # Key is node_id - value is process index of children
        ref = {}
        for i, elem in enumerate(ppid):
            if elem in ref:
                ref[elem].append(i)
            else:
                ref[elem] = [i]

        res = []
        s = [kill]

        while s:
            node = s.pop()  # notice , you don't need to `pop(0)`, it would be slower than pop
            res.append(node)
            if node in ref:
                for elem in ref[node]:
                    s.append(pid[elem])

        return res


if __name__ == '__main__':
    print Solution().killProcess([1, 3, 10, 5], [3, 0, 5, 3], 5)
