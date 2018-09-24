class Solution:
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        rows = len(picture)
        cols = len(picture[0])
        countByRow = [0 for r in range(rows)]
        countByCol = [0 for c in range(cols)]
        lonelyRows = []
        for r in range(rows):
            for c in range(cols):
                if picture[r][c] == 'B':
                    countByRow[r] += 1
                    countByCol[c] += 1
            if countByRow[r] == 1:
                lonelyRows.append(r)
        lonelyCols = []
        for c in range(cols):
            if countByCol[c] == 1:
                lonelyCols.append(c)
        lonely = 0
        for r in lonelyRows:
            for c in lonelyCols:
                if picture[r][c] == 'B':
                    lonely += 1
        return lonely
