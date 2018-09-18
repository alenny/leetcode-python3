# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        myHead = ListNode(0)
        myHead.next = head
        prev, cur = myHead, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        myTail = ListNode(0)
        myTail.next = cur = prev
        prev = myTail
        extra = 1
        while cur != myHead:
            if extra == 1:
                r = cur.val + extra
                cur.val = r % 10
                extra = int(r / 10)
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        myTail.next.next = None
        if extra == 1:
            myHead.val = 1
            return myHead
        return myHead.next


sol = Solution()
ret = sol.plusOne(ListNode(9))
