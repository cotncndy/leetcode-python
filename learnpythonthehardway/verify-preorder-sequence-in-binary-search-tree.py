# Time:  O(n)
# Space: O(1)

# for a preorder sequence of bst, when we do loop, we will firstly arrive root, then its left. assume we push ele into
# stack, it would firstly keep going to left, so it would descends, then if we meet an ele which is larger than
# previous one, which means we see right node of a subtree, , in this case, we keep poping the stack until the top of
#  the
# stack is larger than the curr ele. and we know the last poped one is the root of subtree, let's record it as new
# low, then
# any following node should be larger than this low.

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


if __name__ == '__main__':
    print Solution().verifyPreorder([9, 12, 6])
