class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if not A:
            return 0
        count = 0
        for pos in range(len(A[0])):
            notSorted = False
            for i in range(1, len(A)):
                if A[i][pos] < A[i - 1][pos]:
                    notSorted = True
                    break
            if notSorted:
                count += 1
        return count
