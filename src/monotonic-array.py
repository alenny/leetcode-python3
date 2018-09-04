class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        direction = 0
        for i in range(1, len(A)):
            dirt = A[i] - A[i - 1]
            if direction == 0:
                direction = dirt
            elif direction > 0 and dirt < 0 or direction < 0 and dirt > 0:
                return False
        return True
