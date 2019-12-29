from typing import List

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        N = len(expression)

        def readUnion(idx):
            unions = set()
            while idx < N and expression[idx] != '}':
                prods, idx = readProduct(idx)
                unions.update(prods)
                if idx >= N or expression[idx] == '}':
                    break
                idx += 1    # skip ','
            return unions, idx
                
        def readProduct(idx):
            prods = set([''])
            while idx < N and expression[idx] != ',' and expression[idx] != '}':
                words = set()
                if expression[idx] == '{':
                    words, idx = readUnion(idx + 1)
                    idx += 1    # skip '}'
                else:
                    i = idx
                    while i < N and expression[i] >= 'a' and expression[i] <= 'z':
                        i += 1
                    words.add(expression[idx: i])
                    idx = i
                newProds = set()
                for p in prods:
                    for w in words:
                        newProds.add(p + w)
                prods = newProds
            return prods, idx

        ret = readProduct(0)[0] if expression.startswith('{') else readUnion(0)[0]
        return list(sorted(ret))

sol = Solution()
ret = sol.braceExpansionII("{a,b}{c,{d,e}}")
print(ret)
ret = sol.braceExpansionII("a,b,c")
print(ret)
ret = sol.braceExpansionII("{a},b,c")
print(ret)