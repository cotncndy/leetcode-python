# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if k == 1:
            return root

        head, leng = root, 0
        while head:
            leng, head = leng + 1, head.next
        res, head, tail = [], root, root
        if leng <= k:
            while k:
                res.append(head)
                if head:
                    tail = head.next
                    head.next, head = None, tail
                else:
                    head = None
                k = k - 1
        else:
            d, r = leng / k, leng % k
            while head:
                cnt = d - 1
                if r > 0:
                    cnt, r = cnt + 1, r - 1
                while cnt:
                    tail = tail.next
                    cnt -= 1
                res.append(head)
                head = tail.next
                tail.next = None
                tail = head

        return res


if __name__ == '__main__':
    r0, r1, r2, r3, r4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    r0.next = r1
    r1.next = r2
    r2.next = r3
    r3.next = r4
    print Solution().splitListToParts(None, 3)
