import math


class Solution:
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        dp = [[''] * N for r in range(N)]
        for ln in range(1, N + 1):
            if ln < 5:
                for r in range(N - ln + 1):
                    dp[r][r + ln - 1] = s[r:r + ln]
                continue
            for r in range(N - ln + 1):
                c = r + ln - 1
                src = s[r:c + 1]
                dp[r][c] = src
                for k in range(r, c):
                    t = dp[r][k] + dp[k + 1][c]
                    if len(t) < len(dp[r][c]):
                        dp[r][c] = t
                    kl = k - r + 1
                    count = int(ln / kl)
                    if ln % kl != 0 or count < 2 \
                            or src.replace(s[r:k + 1], '') != '' \
                            or len(dp[r][k]) + len(str(count)) + 2 >= len(dp[r][c]):
                        continue
                    dp[r][c] = '{0}[{1}]'.format(count, dp[r][k])
        return dp[0][N - 1]

    def encodeBacktracking(self, s):
        """
        :type s: str
        :rtype: str
        """
        cache = [dict() for i in range(len(s))]
        return self.encodeHelper(s, 0, len(s), cache)

    def encodeHelper(self, s, begin, end, cache):
        if end - begin < 5:
            return s[begin:end]
        if end in cache[begin]:
            return cache[begin][end]
        shortest = s[begin:end]
        for bi in range(begin, end):
            prefix = s[begin:bi]
            remaining = s[bi:end]
            for ri in range(bi + (end - bi >> 1), bi, -1):
                part, count, j = s[bi:ri], 1, ri
                while s.startswith(part, j):
                    count += 1
                    j += len(part)
                if count == 1:
                    continue
                encodedPart = self.encodeHelper(s, bi, ri, cache)
                for k in range(2, count + 1):
                    combinedParts = self.combinePart(encodedPart, k)
                    if len(combinedParts) >= k * len(part):
                        continue
                    encodedPostfix = self.encodeHelper(
                        s, bi + k * len(part), end, cache)
                    text = combinedParts + encodedPostfix
                    if len(text) < len(remaining):
                        remaining = text
            result = prefix + remaining
            if len(result) < len(shortest):
                shortest = result
        cache[begin][end] = shortest
        return shortest

    def combinePart(self, part, count):
        return '{0}[{1}]'.format(count, part)


sol = Solution()
# ret = sol.encode('abbbabbbcabbbabbbc')
# ret = sol.encode("aaaaaaaaaabbbaaaaabbb")
ret = sol.encode(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print(ret)
