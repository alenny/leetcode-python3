class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        aRows = [[] for r in range(len(A))]
        for r in range(len(A)):
            for c in range(len(A[0])):
                if A[r][c] != 0:
                    aRows[r].append((c, A[r][c]))
        bCols = [[] for c in range(len(B[0]))]
        for c in range(len(B[0])):
            for r in range(len(B)):
                if B[r][c] != 0:
                    bCols[c].append((r, B[r][c]))
        result = [[0 for c in range(len(B[0]))] for r in range(len(A))]
        for r in range(len(A)):
            for c in range(len(B[0])):
                ai, bi = 0, 0
                while ai < len(aRows[r]) and bi < len(bCols[c]):
                    if aRows[r][ai][0] == bCols[c][bi][0]:
                        result[r][c] += aRows[r][ai][1] * bCols[c][bi][1]
                        ai += 1
                        bi += 1
                    elif aRows[r][ai][0] < bCols[c][bi][0]:
                        ai += 1
                    else:
                        bi += 1
        return result


sol = Solution()
ret = sol.multiply([[1, 0, 0], [-1, 0, 3]], [[7, 0, 0], [0, 0, 0], [0, 0, 1]])
