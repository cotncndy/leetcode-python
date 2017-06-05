# Time:  O(nlogk)
# Space: O(1)

# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


# Merge two by two solution.
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy

        heap = []
        for sorted_list in lists:
            if sorted_list:
                # put the head nodes
                # https://docs.python.org/2.7/library/heapq.html#heapq.heappush
                # heap elements can be tuples
                heapq.heappush(heap, (sorted_list.val, sorted_list))

        while heap:
            smallest = heapq.heappop(heap)[1]
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))

        return dummy.next


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list2 = ListNode(2)
    list2.next = ListNode(4)

    print Solution().mergeKLists([list1, list2])
