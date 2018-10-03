import math

class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        maxStep = 6
        board = self.flattenBoard(board)
        end = len(board) - 1
        # BFS
        q = [1]
        visited = [False for i in range(end + 1)]
        visited[1] = True
        moves = 0
        while len(q) > 0:
            nq = []
            for cur in q:
                if cur == end:
                    return moves
                for i in range(1, maxStep + 1):
                    nxt = cur + i
                    if nxt > end:
                        continue
                    if board[nxt] != -1:
                        nxt = board[nxt]
                    if visited[nxt]:
                        continue
                    visited[nxt] = True
                    nq.append(nxt)
            q = nq
            moves += 1
        return -1

    def flattenBoard(self, board):
        ret = [-1]
        colDirection = 1
        size = len(board)
        for r in range(size)[::-1]:
            for c in range(size)[::colDirection]:
                ret.append(board[r][c])
            colDirection = -colDirection
        return ret


sol = Solution()
# ret = sol.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]])
# ret = sol.snakesAndLadders([[-1, 10, -1, 15, -1], [-1, -1, 18, 2, 20],
#                             [-1, -1, 12, -1, -1], [2, 4, 11, 18, 8], [-1, -1, -1, -1, -1]])
# ret = sol.snakesAndLadders([[-1,-1,-1,-1,48,5,-1],[12,29,13,9,-1,2,32],[-1,-1,21,7,-1,12,49],[42,37,21,40,-1,22,12],[42,-1,2,-1,-1,-1,6],[39,-1,35,-1,-1,39,-1],[-1,36,-1,-1,-1,-1,5]])
# ret = sol.snakesAndLadders([[-1, -1, 19, 10, -1], [2, -1, -1, 6, -1],
#                             [-1, 17, -1, 19, -1], [25, -1, 20, -1, -1], [-1, -1, -1, -1, 15]])
ret = sol.snakesAndLadders([[-1,-1,-1,-1,33,-1,-1,-1,-1,37,-1,-1],[-1,-1,-1,17,128,113,11,5,-1,99,-1,-1],[10,-1,72,112,72,31,-1,-1,62,-1,-1,-1],[-1,-1,-1,-1,-1,6,21,122,-1,1,-1,39],[-1,-1,-1,-1,-1,-1,-1,79,-1,128,81,-1],[-1,16,-1,120,-1,-1,11,62,-1,-1,-1,-1],[101,88,87,-1,-1,-1,-1,-1,-1,-1,-1,40],[-1,-1,90,80,-1,-1,-1,-1,-1,-1,-1,35],[-1,78,-1,-1,-1,62,-1,-1,-1,-1,-1,-1],[-1,3,-1,-1,-1,-1,-1,-1,89,-1,-1,-1],[-1,44,-1,-1,-1,103,134,-1,69,-1,-1,123],[-1,24,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]])
print(ret)
