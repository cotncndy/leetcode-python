# Time:  O(n)
# Space: O(1)

# Given a singly linked list, group all odd nodes
# together followed by the even nodes.
# Please note here we are talking about the node number
# and not the value in the nodes.
#
# You should try to do it in place. The program should run
# in O(1) space complexity and O(nodes) time complexity.
#
# Example:
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.
#
# Note:
# The relative order inside both the even and odd groups
# should remain as it was in the input.
# The first node is considered odd, the second node even
# and so on ...

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or (not head.next):
            return head
        pre, cur = head, head.next
        while cur and cur.next:
            temp = pre.next
            pre.next = cur.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
            pre.next = temp

        return head


if __name__ == '__main__':
    li = [1, 2, 3, 4, 5, 6, 7, 8]
    h1 = ListNode(-1)
    h2 = h1
    for idx in xrange(len(li)):
        h1.next = ListNode(li[idx])
        h1 = h1.next

    print Solution().oddEvenList(h2.next)
