class Solution:
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Shit! The interviewer said 1 can directly connect 8 without touching 4,5!
        deps = [None,
                [None, None, [], [2], [], [], [], [4], [], [5]],
                [None, [], None, [], [], [], [], [], [5], []],
                [None, [2], [], None, [], [], [], [5], [], [6]],
                [None, [], [], [], None, [], [5], [], [], []],
                [None, [], [], [], [], None, [], [], [], []],
                [None, [], [], [], [5], [], None, [], [], []],
                [None, [4], [], [5], [], [], [], None, [], [8]],
                [None, [], [5], [], [], [], [], [], None, []],
                [None, [5], [], [6], [], [], [], [8], [], None]]
        total = 0
        for i in range(m, n + 1):
            totalOne = self.helper(deps, set([1]), 1, i - 1)
            totalTwo = self.helper(deps, set([2]), 2, i - 1)
            totalFive = self.helper(deps, set([5]), 5, i - 1)
            total += totalOne * 4 + totalTwo * 4 + totalFive
        return total

    def helper(self, deps, pathSet, prevPos, countLeft):
        if countLeft == 0:
            return 1
        dep = deps[prevPos]
        total = 0
        for j in range(10):
            if dep[j] == None or j in pathSet:
                continue
            hasAllDep = True
            for d in dep[j]:
                if not d in pathSet:
                    hasAllDep = False
                    break
            if not hasAllDep:
                continue
            pathSet.add(j)
            total += self.helper(deps, pathSet, j, countLeft - 1)
            pathSet.remove(j)
        return total
