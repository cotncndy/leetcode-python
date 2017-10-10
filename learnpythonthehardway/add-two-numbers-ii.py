# Time:  O(m + n)
# Space: O(m + n)

# You are given two linked lists representing two non-negative numbers.
# The most significant digit comes first and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        st1, st2 = [], []
        while l1:
            st1.append(l1.val)
            l1 = l1.next

        while l2:
            st2.append(l2.val)
            l2 = l2.next

        sum, head, prv = 0, None, None
        while st1 or st2:
            if st1:
                sum += st1.pop()
            if st2:
                sum += st2.pop()

            head = ListNode(sum % 10)
            head.next = prv
            prv = head
            sum //= 10

        return head


if __name__ == "__main__":
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print Solution().addTwoNumbers(l1, l2)
