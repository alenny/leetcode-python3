class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sums = 0
        products = 1 
        while n > 0:
            d = n % 10
            sums += d
            products *= d
            n = n // 10
        return products - sums