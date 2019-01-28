class Solution:
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        al = len(A)
        xa = [(a, i) for i, a in enumerate(A)]
        xa.sort()
        oddJumps = self.getJumps(xa)
        xa.sort(key=lambda ele: (-ele[0], ele[1]))
        evenJumps = self.getJumps(xa)
        result = set([al-1])
        oq = set([al-1])
        eq = set([al-1])
        while oq or eq:
            noq = set()
            neq = set()
            if oq:
                for oddTarget in oq:
                    neq.update(oddJumps[oddTarget])
            if eq:
                for evenTarget in eq:
                    noq.update(evenJumps[evenTarget])
            result = result.union(neq)
            oq = noq
            eq = neq
        return len(result)

    def getJumps(self, xa):
        jumps = [[] for _ in range(len(xa))]
        stack = [xa[0]]
        for a, i in xa[1:]:
            while stack and stack[-1][1] < i:
                _, fi = stack.pop()
                jumps[i].append(fi)
            stack.append((a, i))
        return jumps


sol = Solution()
# ret = sol.oddEvenJumps([10, 13, 12, 14, 15])
# ret = sol.oddEvenJumps([5, 1, 3, 4, 2])
ret = sol.oddEvenJumps([2, 3, 1, 1, 4])
print(ret)
