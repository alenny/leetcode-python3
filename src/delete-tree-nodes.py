from collections import defaultdict

class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        tree = defaultdict(list)
        root = -1
        for node, par in enumerate(parent):
            tree[par].append(node)
            if par == -1:
                root = node
        nan = 10**6
        dpSums = [nan] * nodes
        toDelete = [False] * nodes
        
        def findNodesToDelete(node):
            if dpSums[node] != nan:
                return dpSums[node]
            sums = value[node]
            for subNode in tree[node]:
                sums += findNodesToDelete(subNode)
            if sums == 0:
                toDelete[node] = True
            dpSums[node] = sums
            return sums
        
        findNodesToDelete(root)

        def markNodesToDelete(node, deleting):
            toDelete[node] |= deleting
            for subNode in tree[node]:
                markNodesToDelete(subNode, toDelete[node])

        markNodesToDelete(root, toDelete[root])
        return toDelete.count(False)