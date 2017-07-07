# Time:  O(n)
# Space: O(1)

# Given a singly linked list, return a random node's value from the linked list.
# Each node must have the same probability of being chosen.
#
# Follow up:
# What if the linked list is extremely large and its length is unknown to you?
# Could you solve this efficiently without using extra space?
#
# Example:
#
# // Init a singly linked list [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
#
# // getRandom() should return either 1, 2, or 3 randomly.
# Each element should have equal probability of returning.
# solution.getRandom();


from random import randint


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.__head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        res = self.__head.val
        curr, num = self.__head.next, 1
        while curr:
            res = curr.val if randint(1, num + 1) == 1 else res
            curr, num = curr.next, num + 1
        return res
