from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        N = len(deck)
        indexes = deque([i for i in range(N)])
        idxRet = []
        while indexes:
            idxRet.append(indexes.popleft())
            if indexes:
                indexes.append(indexes.popleft())
        results = [0 for i in range(N)]
        deck.sort()
        for i in range(N):
            results[idxRet[i]] = deck[i]
        return results


sol = Solution()
ret = sol.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7])
