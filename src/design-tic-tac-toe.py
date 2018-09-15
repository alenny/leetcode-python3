class LaneStatus:
    def __init__(self, n):
        self.zeros = n
        self.players = set()

    def put(self, player):
        self.zeros -= 1
        self.players.add(player)
        return self.__whoWins()

    def __whoWins(self):
        return self.players.pop() if self.zeros == 0 and len(self.players) == 1 else 0


class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.lanes = [LaneStatus(n) for r in range(n + n + 2)]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        ret = self.lanes[row].put(player)
        if ret > 0:
            return ret
        ret = self.lanes[self.n + col].put(player)
        if ret > 0:
            return ret
        if row == col:
            ret = self.lanes[-2].put(player)
            if ret > 0:
                return ret
        if col == self.n - 1 - row:
            ret = self.lanes[-1].put(player)
            if ret > 0:
                return ret
        return 0


# Your TicTacToe object will be instantiated and called as such:
obj = TicTacToe(3)
param_1 = obj.move(1, 0, 1)
param_1 = obj.move(1, 1, 1)
param_1 = obj.move(1, 2, 1)
