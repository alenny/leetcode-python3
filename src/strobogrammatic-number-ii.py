class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        same = ['0', '1', '8']
        exchange = ['0', '1', '6', '8', '9']
        exchangeHead = ['1', '6', '8', '9']
        if n == 0:
            return ['']
        if n == 1:
            return same
        halfLen = n >> 1
        halves = []
        for eh in exchangeHead:
            self.makeHalf(exchange, halfLen - 1, eh, halves)
        ret = []
        if n & 1:
            for half in halves:
                for sm in same:
                    ret.append(half + sm + self.reverseAndReplace(half))
        else:
            for half in halves:
                ret.append(half + self.reverseAndReplace(half))
        return ret

    def makeHalf(self, exchange, n, curr, results):
        if n == 0:
            results.append(curr)
            return
        for ex in exchange:
            self.makeHalf(exchange, n - 1, curr + ex, results)

    def reverseAndReplace(self, str):
        ret = ''
        for i in range(len(str) - 1, -1, -1):
            if str[i] == '6':
                ret += '9'
            elif str[i] == '9':
                ret += '6'
            else:
                ret += str[i]
        return ret
