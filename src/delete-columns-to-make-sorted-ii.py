class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        N = len(A)
        L = len(A[0])
        ret = 0
        q = [[idx for idx in range(N)]]
        pos = 0
        while q and pos < L:
            nq = []
            columnDeleted = False
            for indexes in q:
                prevIdx = indexes[0]
                group = [prevIdx]
                for idx in indexes[1:]:
                    if A[prevIdx][pos] > A[idx][pos]:
                        columnDeleted = True
                        break
                    if A[prevIdx][pos] == A[idx][pos]:
                        group.append(idx)
                        continue
                    if len(group) > 1:
                        nq.append(group)
                    group = [idx]
                    prevIdx = idx
                if columnDeleted:
                    break
                if len(group) > 1:
                    nq.append(group)
            if columnDeleted:
                ret += 1
            else:
                q = nq
            pos += 1
        return ret


sol = Solution()
ret = sol.minDeletionSize(["abx", "agz", "bgc", "bfc"])
print(ret)
