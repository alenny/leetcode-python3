from collections import defaultdict


class Solution:
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        rows = len(picture)
        cols = len(picture[0])
        countByRow = [0 for r in range(rows)]
        countByCol = [0 for c in range(cols)]
        nbRows = []
        rowContentMap = defaultdict(set)
        for r in range(rows):
            rowContentMap[str(picture[r])].add(r)
            for c in range(cols):
                if picture[r][c] == 'B':
                    countByRow[r] += 1
                    countByCol[c] += 1
            if countByRow[r] == N:
                nbRows.append(r)
        nbCols = []
        for c in range(cols):
            if countByCol[c] == N:
                nbCols.append(c)
        ret = 0
        for r in nbRows:
            for c in nbCols:
                if picture[r][c] != 'B':
                    continue
                sameRows = rowContentMap[str(picture[r])]
                valid = True
                for r1 in range(rows):
                    if picture[r1][c] == 'B' and not r1 in sameRows:
                        valid = False
                        break
                if valid:
                    ret += 1
        return ret
