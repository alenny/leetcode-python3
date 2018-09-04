class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.rows = len(vec2d)
        self.currRow = 0
        self.currCol = -1
        self.goToNext()

    def next(self):
        """
        :rtype: int
        """
        ret = self.vec2d[self.currRow][self.currCol]
        self.goToNext()
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.currRow < self.rows and self.currCol < len(self.vec2d[self.currRow])

    def goToNext(self):
        while self.currRow < self.rows and self.currCol >= len(self.vec2d[self.currRow]) - 1:
            self.currRow += 1
            self.currCol = -1
        self.currCol += 1

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
