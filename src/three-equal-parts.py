class Solution:
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        AS = ''.join(map(str, A))
        l, r = 0, N - 1
        lOnes, rOnes = 0 if AS[l] == '0' else 1, 0 if AS[r] == '0' else 1
        while l < r - 1:
            if lOnes < rOnes:
                l += 1
                lOnes += 1 if AS[l] == '1' else 0
                continue
            if lOnes > rOnes:
                r -= 1
                rOnes += 1 if AS[r] == '1' else 0
                continue
            # lOnes == rOnes
            if not self.sameBinary(AS, 0, l, r, N - 1):
                l += 1
                lOnes += 1 if AS[l] == '1' else 0
                continue
            # sameBinary(left, right) == True
            if self.sameBinary(AS, 0, l, l + 1, r - 1):
                return [l, r]
            r -= 1
            while l < r - 1 and AS[r] == '0':
                if self.sameBinary(AS, 0, l, l + 1, r - 1):
                    return [l, r]
                r -= 1
            rOnes += 1
        return [-1, -1]

    def sameBinary(self, AS, b0, e0, b1, e1):
        s0 = AS[b0:e0 + 1]
        s1 = AS[b1:e1 + 1]
        if len(s0) > len(s1):
            s0, s1 = s1, s0
        s0 = '0' * (len(s1) - len(s0)) + s0
        return s0 == s1


sol = Solution()
ret = sol.threeEqualParts([1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0])
print(ret)
