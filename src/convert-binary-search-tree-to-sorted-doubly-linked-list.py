# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        head, tail = self.traverse(root)
        if head:
            head.left = tail
            tail.right = head
        return head

    def traverse(self, node):
        if not node:
            return (None, None)
        leftHead, leftTail = self.traverse(node.left)
        rightHead, rightTail = self.traverse(node.right)
        node.left = leftTail
        if leftTail:
            leftTail.right = node
        node.right = rightHead
        if rightHead:
            rightHead.left = node
        return (leftHead if leftHead else node, rightTail if rightTail else node)


root = Node(4, Node(2, Node(1, None, None), Node(
    3, None, None)), Node(5, None, None))
sol = Solution()
ret = sol.treeToDoublyList(root)
