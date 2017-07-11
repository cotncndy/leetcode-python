# Time:  O(n)
# Space: O(1)
#
# Given a singly linked list L: L0->L1->...->Ln-1->Ln,
# reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...
#
# You must do this in-place without altering the nodes' values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None or head.next is None:
            return head

        fast, slow, prev = head, head, None
        while fast and fast.next:
            fast, slow, prev = fast.next.next, slow.next, slow

        # curr, prev, prev.next = prev, None, None review AttributeError: 'NoneType' object has no attribute 'next'
        # break the list from the middle
        curr, prev.next, prev = slow, None, None

        while curr is not None:  # review how to reverse a linkedlist by using just one sentence
            curr.next, prev, curr = prev, curr, curr.next

        l1, l2 = head, prev
        dummy = ListNode(-1)
        curr = dummy

        while l1 is not None and l2 is not None:
            curr.next, curr, l1 = l1, l1, l1.next
            curr.next, curr, l2 = l2, l2, l2.next

        return dummy.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution().reorderList(head)
