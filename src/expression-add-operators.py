from collections import defaultdict


class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        cache = [defaultdict(dict) for i in range(len(num))]
        return self.addHelper(num, len(num) - 1, target, 1, cache)

    def addHelper(self, num, idx, target, postProduct, cache):
        if postProduct in cache[idx][target]:
            return cache[idx][target][postProduct]
        if idx == 0:
            x = int(num[0])
            return [num[0]] if target == x * postProduct else []
        ret = []
        if num[0] != '0':
            whole = num[0:idx + 1]
            if target == int(whole) * postProduct:
                ret.append(whole)
        for begin in range(1, idx + 1):
            if num[begin] == '0' and begin != idx:
                continue
            strCur = num[begin:idx + 1]
            curNum = int(strCur) * postProduct
            # *
            subRet = self.addHelper(
                num, begin - 1, target, curNum, cache)
            for s in subRet:
                ret.append(s + '*' + strCur)
            # +
            subRet = self.addHelper(num, begin - 1, target - curNum, 1, cache)
            for s in subRet:
                ret.append(s + '+' + strCur)
            # -
            subRet = self.addHelper(num, begin - 1, curNum + target, 1, cache)
            for s in subRet:
                ret.append(s + '-' + strCur)
        cache[idx][target][postProduct] = ret
        return ret


sol = Solution()
# ret = sol.addOperators('123', 6)
# ret = sol.addOperators('232', 8)
# ret = sol.addOperators('105', 5)
# ret = sol.addOperators('00', 0)
# ret = sol.addOperators('3456237490', 9191)
ret = sol.addOperators("123456789", 45)
print(ret)
