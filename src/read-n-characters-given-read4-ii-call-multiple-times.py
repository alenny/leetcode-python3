# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

from collections import deque


class Solution(object):
    def __init__(self):
        self.globalBuf = deque()

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        buf4 = [''] * 4
        while len(self.globalBuf) < n:
            ret = read4(buf4)
            for i in range(ret):
                self.globalBuf.append(buf4[i])
            if ret < 4:
                break
        i = 0
        while i < n and len(self.globalBuf) > 0:
            buf[i] = self.globalBuf.popleft()
            i += 1
        return i
