from random import randint


class Solution:

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.rows = n_rows
        self.cols = n_cols
        self.used = set()

    def flip(self):
        """
        :rtype: List[int]
        """
        while True:
            r = randint(0, self.rows - 1)
            c = randint(0, self.cols - 1)
            key = self.posKey(r, c)
            if key in self.used:
                continue
            self.used.add(key)
            return [r, c]

    def reset(self):
        """
        :rtype: void
        """
        self.used = set()

    def posKey(self, r, c):
        return '{},{}'.format(r, c)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
