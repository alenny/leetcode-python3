class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        r = color[1:3]
        g = color[3:5]
        b = color[5:]
        return '#' + self.__nearest(r) + self.__nearest(g) + self.__nearest(b)

    def __nearest(self, hx):
        if hx[0] == hx[1]:
            return hx
        origin = int(hx, 16)
        xs = hx[0] + hx[0]
        x = int(xs, 16)
        ys0 = hex(
            int(hx[0], 16) + 1)[2:] if hx[0] < hx[1] else hex(int(hx[0], 16) - 1)[2:]
        ys = ys0 + ys0
        y = int(ys, 16)
        return xs if abs(x - origin) < abs(y - origin) else ys
