# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution:
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        # get deepest depth
        deepest = self.getDepth(nestedList, 0)
        # calculate
        return self.summarize(nestedList, deepest)

    def getDepth(self, nestedList, prevDep):
        deepest = prevDep + 1
        for ni in nestedList:
            if not ni.isInteger():
                deepest = max(deepest, self.getDepth(
                    ni.getList(), prevDep + 1))
        return deepest

    def summarize(self, nestedList, curDep):
        total = 0
        for ni in nestedList:
            if ni.isInteger():
                total += curDep * ni.getInteger()
            else:
                total += self.summarize(ni.getList(), curDep - 1)
        return total
