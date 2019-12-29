"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ret = []
        f = customfunction.f
        maxR = 1000
        for x in range(1, 1001):
            l, r = 1, maxR
            while l <= r:
                y = (l + r) // 2
                fr = f(x, y) 
                if fr == z:
                    ret.append([x, y])
                    maxR = y - 1
                    break
                if fr > z:
                    r = y - 1 
                else:
                    l = y + 1
        return ret