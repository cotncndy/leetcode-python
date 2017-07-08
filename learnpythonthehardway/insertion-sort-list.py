# Time:  O(n ^ 2)
# Space: O(1)
#
# Sort a linked list using insertion sort.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))
        else:
            return "Nil"


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None or self.isSorted(head):
            return head

        res = ListNode(-1)
        cur = res
        while head:
            next = head.next
            cur = res
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            head.next = cur.next
            cur.next = head
            head = next
        return res.next

    def isSorted(self, head):
        while head and head.next:
            if head.val > head.next.val:
                return False
            head = head.next
        return True


if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(1)
    print Solution().insertionSortList(head)
