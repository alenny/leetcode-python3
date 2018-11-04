class RecentCounter:

    def __init__(self):
        self.window = 3000
        self.times = []
        self.begin = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.times.append(t)
        while self.begin < len(self.times) and self.times[self.begin] < t - self.window:
            self.begin += 1
        return len(self.times) - self.begin


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
