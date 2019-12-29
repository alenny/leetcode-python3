class Solution:
    def lastSubstring(self, s: str) -> str:
        # The result must be a string with non-ascending sequence

        N = len(s)

        def compare(b1, b2):
            while b1 < N and b2 < N:
                if s[b1] < s[b2]:
                    return -1
                if s[b1] > s[b2]:
                    return 1
                b1 += 1
                b2 += 1
            return 1 if b1 < b2 else -1

        descStarts = []
        i = 0
        while i < N:
            b = i
            i += 1
            while i < N and s[i] <= s[i - 1]:
                i += 1
            descStarts.append(b)
        retB = descStarts[0]
        for b in descStarts[1:]:
            if compare(b, retB) > 0:
                retB = b
        return s[retB:]

    def lastSubstring1(self, s: str) -> str:
        N = len(s)
        maxSub = ''
        for i in range(N):
            ss = s[i:]
            if (ss > maxSub):
                maxSub = ss
        return maxSub

sol = Solution()
ret = sol.lastSubstring("cacacb")
print(ret)