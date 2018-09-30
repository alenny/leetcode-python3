"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        newNode = Node(insertVal, None)
        if not head:
            newNode.next = newNode
            return newNode
        if head.next == head:
            head.next = newNode
            newNode.next = head
            return head
        node = head.next
        while node != head:
            if node.val > insertVal:
                if node.next.val < node.val and node.next.val > insertVal:
                    self.insertNode(newNode, node)
                    return head
                node = node.next
            elif node.val < insertVal:
                if node.next.val < node.val or node.next.val > insertVal:
                    self.insertNode(newNode, node)
                    return head
                node = node.next
            else:
                self.insertNode(newNode, node)
                return head
        self.insertNode(newNode, head)
        return head

    def insertNode(self, newNode, node):
        newNode.next = node.next
        node.next = newNode
