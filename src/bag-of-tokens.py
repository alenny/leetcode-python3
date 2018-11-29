class Solution:
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        if len(tokens) == 0:
            return 0
        tokens.sort()
        points, l, r = 0, 0, len(tokens) - 1
        while l < r:
            if P >= tokens[l]:
                points += 1
                P -= tokens[l]
                l += 1
            elif not points:
                break
            else:
                points -= 1
                P += tokens[r]
                r -= 1
        if l == r and P >= tokens[l]:
            points += 1
        return points
