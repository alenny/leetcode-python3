# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.vals = set()
        def traverse(node, parentVal, plus):
            if not node:
                return
            node.val = 2 * parentVal + plus
            self.vals.add(node.val)
            traverse(node.left, node.val, 1)
            traverse(node.right, node.val, 2)
            return
        traverse(root, 0, 0)

    def find(self, target: int) -> bool:
        return target in self.vals


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)