# Time:  O(n)
# Space: O(logn)
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    head = None

    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return head
        slow, fast = head, head
        last = slow
        while fast.next and fast.next.next:  # bugfixed
            last, slow, fast = slow, slow.next, fast.next.next
        # split the origina list to halves
        last.next, fast = None, slow.next
        cur = TreeNode(slow.val)

        cur.left = self.sortedListToBST(head)
        cur.right = self.sortedListToBST(fast)

        return cur


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    result = Solution().sortedListToBST(head)
    print result.val
    print result.left.val
    # print result.right.val
