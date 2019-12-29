class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        temp = []
        leftCount = 0
        for ch in s:
            if ch == '(':
                leftCount += 1
                temp.append(ch)
            elif ch == ')':
                if leftCount > 0:
                    leftCount -= 1
                    temp.append(ch)
            else:
                temp.append(ch)
        ret = []
        rightCount = 0
        for ch in temp[::-1]:
            if ch == ')':
                rightCount += 1
                ret.append(ch)
            elif ch == '(':
                if rightCount > 0:
                    rightCount -= 1
                    ret.append(ch)
            else:
                ret.append(ch)
        return ''.join(reversed(ret))