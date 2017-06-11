# Time:  O(n)
# Space: O(1)

class Solution:
    # @param {integer[]} preorder
    # @return {boolean}
    def verifyPreorder(self, preorder):
        low, stack = float("-inf"), []

        for i in preorder:
            if i < low:
                return False
            while stack and i > stack[-1]:
                low = stack.pop()

            stack.append(i)
        return True
