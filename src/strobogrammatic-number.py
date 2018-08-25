class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] == '6' and num[right] == '9' or \
                    num[left] == '9' and num[right] == '6' or \
                    num[left] == '1' and num[right] == '1' or \
                    num[left] == '8' and num[right] == '8' or \
                    num[left] == '0' and num[right] == '0':
                left += 1
                right -= 1
                continue
            return False
        return True
