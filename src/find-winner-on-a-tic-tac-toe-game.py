class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        moveCount = len(moves)
        winningCombs = [
            [ (0, 0), (0, 1), (0, 2)],
            [ (1, 0), (1, 1), (1, 2)],
            [ (2, 0), (2, 1), (2, 2)],
            [ (0, 0), (1, 0), (2, 0)],
            [ (0, 1), (1, 1), (2, 1)],
            [ (0, 2), (1, 2), (2, 2)],
            [ (0, 0), (1, 1), (2, 2)],
            [ (0, 2), (1, 1), (2, 0)]
        ]
        i = 0
        A = set()
        B = set()
        while i < moveCount:
            A.add((moves[i][0], moves[i][1]))
            i += 1
            if i < moveCount:
                B.add((moves[i][0], moves[i][1]))
            i += 1
        for comb in winningCombs:
            winA = True
            winB = True
            for rc in comb:
                winA = winA and (rc in A)
                winB = winB and (rc in B)
            if winA:
                return 'A'
            if winB:
                return 'B'
        return 'Pending' if moveCount < 9 else 'Draw'
                