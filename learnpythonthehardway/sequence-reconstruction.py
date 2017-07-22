# Time:  O(n * s), n is the size of org, s is the size of seqs
# Space: O(n)

class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if len(org) == 0 or len(seqs) == 0:
            return False
        position, visited, count = [0] * (len(org) + 1), [False] * (len(org) + 1), len(org) - 1  # bugfixed

        for i, k in enumerate(org):
            position[k] = i

        for seq in seqs:
            for i, k in enumerate(seq):
                if not 0 < k <= len(org):
                    return False  # [4,1,5,2,6,3], [1,7] is illegal
                if not i:  # i==0 continue
                    continue
                prev, cur = position[seq[i - 1]], position[k]
                if prev >= cur:
                    return False
                if not visited[cur] and prev + 1 == cur:  # if cur is already arranged, no need to do anything
                    visited[cur], count = True, count - 1

        return count == 0


if __name__ == '__main__':
    print Solution().sequenceReconstruction([4, 1, 5, 2, 6, 3], [[5, 2, 6, 3], [4, 1, 5, 2]])
