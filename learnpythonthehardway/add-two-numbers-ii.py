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

        while l2:
            st2.append(l2.val)

        sum, head = 0, None
        while st1 or st2:
            if st1:
                sum += st1
            if st2:
                sum += st2

            head.val = sum % 10
            res = ListNode(sum / 10)
            res.next = head
            head = res
            sum /= 10

        return head if head.val == 0 else head.next
