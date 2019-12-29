# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ret = 0
        while head:
            ret = (ret << 1) + head.val
            head = head.next
        return ret