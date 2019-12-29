import math

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)
        tc = N / 4
        i = 0
        while i < N:
            bi = i
            while i < N and arr[i] == arr[bi]:
                i += 1
            c = i - bi
            if c > tc:
                return arr[bi]
        raise 'no result'