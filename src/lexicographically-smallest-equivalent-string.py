class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        groups = dict()
        giMap = dict()
        nextGi = 0
        for a, b in zip(A, B):
            if not a in giMap and not b in giMap:
                giMap[a] = giMap[b] = nextGi
                groups[nextGi] = set([a, b])
                nextGi += 1
            elif not a in giMap:
                giMap[a] = giMap[b]
                groups[giMap[b]].add(a)
            elif not b in giMap:
                giMap[b] = giMap[a]
                groups[giMap[a]].add(b)
            else:
                giA, giB = giMap[a], giMap[b]
                groups[giA] = groups[giA].union(groups[giB])
                for ch in groups[giB]:
                    giMap[ch] = giA
        minChars = dict()
        for gi, charSet in groups.items():
            minChars[gi] = min(charSet)
        retArr = []
        for ch in S:
            if not ch in giMap:
                retArr.append(ch)
            else:
                retArr.append(minChars[giMap[ch]])
        return ''.join(retArr)
