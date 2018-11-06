class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        # find all consequent 0s
        zeros = [0]
        for a in A:
            if a == 1:
                zeros.append(0)
            else:
                zeros[-1] += 1
        total = 0
        if S == 0:
            for count in zeros:
                total += (count * (count + 1) >> 1)
        else:
            for left in range(len(zeros) - S):
                right = left + S
                total += (zeros[left] + 1) * (zeros[right] + 1)
        return total
