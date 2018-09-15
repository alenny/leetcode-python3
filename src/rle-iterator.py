class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A
        self.cursor = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.cursor < len(self.A):
            if n <= self.A[self.cursor]:
                self.A[self.cursor] -= n
                ret = self.A[self.cursor + 1]
                if self.A[self.cursor] == 0:
                    self.cursor += 2
                return ret
            # n > self.A[self.cursor]:
            n -= self.A[self.cursor]
            self.cursor += 2
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
