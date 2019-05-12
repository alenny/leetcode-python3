class Solution:
    def camelMatch(self, queries, pattern: str):
        ret = []
        pN = len(pattern)
        for q in queries:
            pi, qi = 0, 0
            qN = len(q)
            while pi < pN and qi < qN:
                if pattern[pi] == q[qi]:
                    pi += 1
                    qi += 1
                elif self._isUpcase(q[qi]):
                    break
                else:
                    qi += 1
            if pi < pN:
                ret.append(False)
                continue
            while qi < qN and not self._isUpcase(q[qi]):
                qi += 1
            ret.append(qi == qN)
        return ret

    def _isUpcase(self, ch):
        return ord(ch) >= ord('A') and ord(ch) <= ord('Z')


sol = Solution()
ret = sol.camelMatch(["FooBar", "FooBarTest", "FootBall",
                      "FrameBuffer", "ForceFeedBack"], "FB")
print(ret)
ret = sol.camelMatch(["FooBar", "FooBarTest", "FootBall",
                      "FrameBuffer", "ForceFeedBack"], "FoBa")
print(ret)
ret = sol.camelMatch(["FooBar", "FooBarTest", "FootBall",
                      "FrameBuffer", "ForceFeedBack"], "FoBaT")
print(ret)
