from collections import defaultdict

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        chMap = defaultdict(list)
        for i, ch in enumerate(str1):
            chMap[ch].append(i)
        chSet2 = set(list(str2))
        if len(chMap) == 26 and len(chSet2) == 26 and str1 != str2:
            return False        
        for idxs in chMap.values():
            ch = str2[idxs[0]]
            for i in idxs[1:]:
                if ch != str2[i]:
                    return False
        return True

sol = Solution()
ret = sol.canConvert("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza")
print(ret)
ret = sol.canConvert("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyzq")
print(ret)