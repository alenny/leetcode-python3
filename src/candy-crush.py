from collections import defaultdict


class Solution:
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        self.rows = len(board)
        self.cols = len(board[0])
        while self.helper(board):
            pass
        return board

    def helper(self, board):
        changes = defaultdict(set)
        for r in range(self.rows):
            same = 1
            for c in range(1, self.cols + 1):
                if c < self.cols and board[r][c] == board[r][c - 1] and board[r][c] != 0:
                    same += 1
                else:
                    if same >= 3:
                        for c1 in range(c - same, c):
                            changes[c1].add(r)
                    same = 1
        for c in range(self.cols):
            same = 1
            for r in range(1, self.rows + 1):
                if r < self.rows and board[r][c] == board[r - 1][c] and board[r][c] != 0:
                    same += 1
                else:
                    if same >= 3:
                        for r1 in range(r - same, r):
                            changes[c].add(r1)
                    same = 1
        if len(changes) == 0:
            return False
        for c, changedRows in changes.items():
            drop = 0
            for r in range(self.rows - 1, -1, -1):
                if r in changedRows:
                    drop += 1
                    continue
                board[r + drop][c] = board[r][c]
            for r in range(drop):
                board[r][c] = 0
        return True

sol = Solution()
ret = sol.candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]])
print('ok')