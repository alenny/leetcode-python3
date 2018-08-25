# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):


def read4(buf):
    return 0    # dummy code


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        total = 0
        while total < n:
            buf4 = [0 for i in range(4)]
            len4 = read4(buf4)
            copyLen = min(len4, n - total)
            for i in range(copyLen):
                buf[total + i] = buf4[i]
            total += copyLen
            if len4 < 4:
                break
        return total
