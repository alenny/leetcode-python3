# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        l = 0
        node = head
        while node:
            l += 1
            node = node.next
        stack = []
        ret = [0] * l
        j = 0
        while head:
            while stack and head.val > stack[-1][1].val:
                i = stack.pop()[0]
                ret[i] = head.val
            stack.append((j, head))
            head = head.next
            j += 1
        return ret
