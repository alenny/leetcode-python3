class SnakeGame:

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.cols = width
        self.rows = height
        self.grid = [dict() for r in range(self.rows)]
        self.trace = [[0, 0]]
        self.bodyLength = 1
        self.grid[0][0] = 1  # 0: nothing, 1: snake body, 2: food
        self.food = food
        if len(self.food) > 0:
            fr, fc = food[0]
            self.grid[fr][fc] = 2
        self.nextFoodIdx = 1
        self.directMap = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        direct = self.directMap[direction]
        currPos = self.trace[-1]
        tr, tc = currPos[0] + direct[0], currPos[1] + direct[1]
        if tr < 0 or tr >= self.rows or tc < 0 or tc >= self.cols \
                or tc in self.grid[tr] and self.grid[tr][tc] == 1 and [tr, tc] != self.trace[-self.bodyLength]:
            return -1
        foodEaten = False
        if tc in self.grid[tr] and self.grid[tr][tc] == 2:
            foodEaten = True
            self.bodyLength += 1
        self.trace.append([tr, tc])
        if len(self.trace) > self.bodyLength:
            pr, pc = self.trace[-self.bodyLength - 1]
            if pc in self.grid[pr]:
                self.grid[pr].pop(pc)
        self.grid[tr][tc] = 1
        if foodEaten and self.nextFoodIdx < len(self.food):
            nfr, nfc = self.food[self.nextFoodIdx]
            if nfr >= 0 and nfr < self.rows and nfc >= 0 and nfc < self.cols:
                self.grid[nfr][nfc] = 2
            self.nextFoodIdx += 1
        return self.bodyLength - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

# game = SnakeGame(3, 2, [[1, 2], [0, 1]])
# moves = [["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]

game = SnakeGame(100, 30, [[11,0],[58,7]])
moves = [["D"],["R"],["R"],["D"],["D"],["U"],["D"],["R"],["L"],["R"],["U"],["D"],["D"],["R"],["R"],["U"],["D"],["R"],["D"],["D"],["D"],["D"],["U"],["D"],["L"],["D"],["U"],["D"],["U"],["D"],["R"],["L"],["L"],["R"],["D"],["L"],["U"],["L"],["L"],["L"],["R"],["R"],["U"],["R"],["L"],["D"],["R"],["L"],["U"],["U"],["D"],["D"],["D"],["L"],["L"],["D"],["L"],["D"],["R"],["U"],["L"],["U"],["R"],["R"],["U"],["L"],["D"],["L"],["D"],["D"]]

for i in range(len(moves)):
    game.move(moves[i][0])

print('ok')
