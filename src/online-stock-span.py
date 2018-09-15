class StockSpanner:

    def __init__(self):
        self.prices = []
        self.spans = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        i = len(self.prices) - 1
        while i >= 0:
            if self.prices[i] > price:
                break
            span += self.spans[i]
            i -= self.spans[i]
        self.prices.append(price)
        self.spans.append(span)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
