from typing import List

class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        count = len(chips)
        evenCount = 0
        for c in chips:
            if c % 2 == 0:
                evenCount += 1
        return min(count - evenCount, evenCount)