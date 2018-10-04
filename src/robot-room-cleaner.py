# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class MyRobot:
    def __init__(self, robot, x, y, direction):
        self.__directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.__robot = robot
        self.direction = direction  # 0: up, 1: right, 2: down, 3: left
        self.x = x
        self.y = y

    def move(self):
        ret = self.__robot.move()
        if ret:
            dx, dy = self.__directions[self.direction]
            self.x += dx
            self.y += dy
        return ret

    def turnLeft(self):
        self.__robot.turnLeft()
        self.direction = 3 if self.direction == 0 else self.direction - 1

    def turnRight(self):
        self.__robot.turnRight()
        self.direction = 0 if self.direction == 3 else self.direction + 1

    def clean(self):
        self.__robot.clean()

    def getNeighbors(self):
        return [(self.x + dx, self.y + dy) for dx, dy in self.__directions]

    def turnTo(self, direction):
        change = direction - self.direction
        if change == 1 or change == -3:
            self.turnRight()
        elif change == -1 or change == 3:
            self.turnLeft()
        elif change != 0:
            self.turnRight()
            self.turnRight()


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        rob = MyRobot(robot, 0, 0, 0)
        self.dfs(rob, [(rob.x, rob.y)], set([self.posKey(rob.x, rob.y)]))

    def dfs(self, rob, path, visited):
        rob.clean()
        for direction, (nx, ny) in enumerate(rob.getNeighbors()):
            nKey = self.posKey(nx, ny)
            if nKey in visited:
                continue
            visited.add(nKey)
            rob.turnTo(direction)
            if rob.move():
                path.append((rob.x, rob.y))
                self.dfs(rob, path, visited)
                path.pop()
                rob.turnTo(direction + 2 if direction < 2 else direction - 2)
                rob.move()

    def posKey(self, x, y):
        return '{0},{1}'.format(x, y)
