# Time:  O(n)
# Space: O(1)
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space.
# You may not modify the values in the list, only nodes itself can be changed.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(-1)
        dummy.next = head

        cur, pre = head, dummy

        while cur and cur.next:
            temp = cur.next
            cur.next = temp.next
            temp.next, pre.next = pre.next, temp
            pre, cur = cur, cur.next

        return dummy.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next, head.next.next, head.next.next.next = ListNode(2), ListNode(3), ListNode(4)
    print Solution().swapPairs(head)
