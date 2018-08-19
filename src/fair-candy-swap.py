class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        setA = set()
        for a in A:
            setA.add(a)
        diff = sum(A) - sum(B) >> 1
        for b in B:
            if b + diff in setA:
                return [b + diff, b]
        return []
