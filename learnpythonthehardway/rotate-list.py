# Time:  O(n)
# Space: O(1)
#
# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        n, cur = 0, head
        while cur:
            cur = cur.next
            n += 1
        # link to be a loop
        cur.next = head
        cur, tail = head, cur
        for _ in xrange(n - k % n):
            tail = cur
            cur = cur.next
        tail.next = None

        return cur
