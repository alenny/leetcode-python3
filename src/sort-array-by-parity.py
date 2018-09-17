class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(A) - 1
        while left < right:
            if (A[left] & 1) == 0:
                left += 1
                continue
            if (A[right] & 1) == 1:
                right -= 1
                continue
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
        return A
