# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        stack = [head]
        prev = None
        while len(stack) > 0:
            cur = stack.pop()
            if prev:
                cur.prev = prev
                prev.next = cur
            while cur:
                if cur.child:
                    if cur.next:
                        stack.append(cur.next)
                    cur.next = cur.child
                    cur.child = None
                    cur.next.prev = cur
                prev = cur
                cur = cur.next
        return head
