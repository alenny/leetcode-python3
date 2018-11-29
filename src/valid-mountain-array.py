class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        state = 0
        for i in range(1, len(A)):
            if A[i] == A[i - 1] or A[i] > A[i - 1] and state == 2 or A[i] < A[i - 1] and state == 0:
                return False
            if A[i] > A[i - 1] and state == 0:
                state = 1
            elif A[i] < A[i - 1] and state == 1:
                state = 2
        return state == 2
