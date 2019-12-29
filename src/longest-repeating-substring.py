class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        # similar as method 1, but decrease the time from O(n^2) to O(nlogn) by using binary search on len(S)
        N = len(S)

        def findDuplicate(L: int) -> bool:
            words = set()
            for i in range(N - L + 1):
                w = S[i:i + L]
                if w in words:
                    return True
                words.add(w)
            return False

        left, right = 0, N
        while left <= right:
            mid = left + right >> 1
            if findDuplicate(mid):
                left = mid + 1
            else:
                right = mid - 1
            
        return max(0, left - 1)

    def longestRepeatingSubstring1(self, S: str) -> int:
        # accepted, but very slow
        N = len(S)
        words = set()
        for n in range(1, N)[::-1]:
            for i in range(N - n + 1):
                w = S[i:i + n]
                if w in words:
                    return n
                words.add(w)
        return 0                

    def longestRepeatingSubstring2(self, S: str) -> int:
        # timeout 
        N = len(S)
        dp = [0, 0]
        for i in range(2, N + 1):
            n = i
            while n > 0:
                target = S[i - n:i]
                pos = S.index(target)
                if pos != i - n:
                    break
                n -= 1
            dp.append(n)
        return max(dp)

sol = Solution()
ret = sol.longestRepeatingSubstring('aaaaa')
print(ret)


