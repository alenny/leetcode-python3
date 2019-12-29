class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        N = len(customers)
        lastXDiff = 0
        total = 0
        i = 0
        while i < X:
            if grumpy[i] == 1:
                lastXDiff += customers[i]
            else:
                total += customers[i]
            i += 1
        maxXDiff = lastXDiff
        while i < N:
            j = i - X
            if grumpy[j] == 1:
                lastXDiff -= customers[j]
            if grumpy[i] == 1:
                lastXDiff += customers[i]
            else:
                total += customers[i]
            if lastXDiff > maxXDiff:
                maxXDiff = lastXDiff
            i += 1
        return total + maxXDiff