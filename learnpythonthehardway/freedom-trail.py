#  In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the
# "Freedom Trail Ring", and use the dial to spell a specific keyword in order to open the door.
#
# Given a string ring, which represents the code engraved on the outer ring and another string key, which represents
# the keyword needs to be spelled. You need to find the minimum number of steps in order to spell all the characters
# in the keyword.
# Initially, the first character of the ring is aligned at 12:00 direction. You need to spell all the characters in
# the string key one by one by rotating the ring clockwise or anticlockwise to make each character of the string key
# aligned at 12:00 direction and then by pressing the center button.
# At the stage of rotating the ring to spell the key character key[i]:
#
#     You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. The final purpose of the
# rotation is to align one of the string ring's characters at the 12:00 direction, where this character must equal to
#  the character key[i].
#     If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell,
# which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next
# stage), otherwise, you've finished all the spelling.
#
# Example:
#
#
# https://leetcode.com/static/images/problemset/ring.jpg
#
# Note:
#
#     Length of both ring and key will be in range 1 to 100.
#     There are only lowercase letters in both strings and might be some duplcate characters in both strings.
#     It's guaranteed that string key could always be spelled by rotating the string ring.
#
#
# Input: ring = "godding", key = "gd"
# Output: 4
# Explanation:
#  For the first key character 'g', since it is already in place, we just need 1 step to spell this character.
#  For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it
# become "ddinggo".
#  Also, we need 1 more step for spelling.
#  So the final output is 4.
import collections


class Solution(object):
    minStep = float('inf')


    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        dict = collections.defaultdict(set)
        memo = collections.defaultdict(int)

        for k, v in enumerate(ring):
            dict[v].add(k)

        # return self.dfs(ring, key, dict, 0, 0, "", memo)

        return self.dfs2(ring, key, dict, 0, memo)

        # return self.minStep

    def dfs(self, ring, key, dict, pos, step, st, memo):
        if pos == len(key):
            if st not in memo or step < memo[st]:
                memo[st] = step
            # if step < self.minStep:
            #     self.minStep = step
            return step

        if st in memo:
            return memo[st]

        cSet, tep = dict[key[pos]], float('inf')
        for p in cSet:
            adjust = min(p, len(ring) - p)
            tStep = step + adjust + 1
            if tStep > self.minStep:  # prunning
                continue
            # https://stackoverflow.com/questions/2465921/how-to-copy-a-dictionary-and-only-edit-the-copy
            dict2 = dict.copy()  # knowledge how to copy a dict
            res = ""
            if adjust == p:  # rotate anti-clock
                res = self.reset(ring, dict2, -p)
            else:
                res = self.reset(ring, dict2, len(ring) - p)

            tep = min(tep, self.dfs(ring, key, dict2, pos + 1, tStep, res, memo))
            memo[res] = min(tep, memo[res]) if res in memo else tep

        memo[st] = tep
        return tep

    def dfs2(self, ring, key, dict, pos, memo):
        if pos == len(key):
            return 0
        if ring in memo:
            return memo[ring]

        cSet = dict[key[pos]]
        res = float('inf')
        for p in cSet:
            adjust = min(p, len(ring) - p)
            dict2 = dict.copy()  # knowledge how to copy a dict
            st = ""
            if adjust == p:  # rotate anti-clock
                st = self.reset(ring, dict2, -p)
            else:
                st = self.reset(ring, dict2, len(ring) - p)

            res = min(adjust + self.dfs2(st, key, dict2, pos + 1, memo), res)

        memo[ring] = res + 1
        return memo[ring]


    def reset(self, ring, dict, adjust):
        list = [''] * len(ring)
        for k, v in dict.iteritems():
            temp = set()
            for s in v:
                s = (s + adjust) % len(ring)
                s = s + len(ring) if s < 0 else s
                temp.add(s)
                list[s] = k
            dict[k] = temp
        return ''.join(list)


if __name__ == '__main__':
    # print Solution().findRotateSteps("godding", "gd")
    # print Solution().findRotateSteps("godding", "gdi")
    print Solution().findRotateSteps("godding", "ggn")
    # print Solution().findRotateSteps("godding", "gni")
    # print Solution().findRotateSteps("godding", "ndi")
    # print Solution().findRotateSteps("caotmcaataijjxi", "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx")
