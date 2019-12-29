class Solution:
    def expand(self, S: str) -> List[str]:
        sl = len(S)
        levels = []
        i = 0
        while i < sl:
            levels.append([])
            if S[i] != '{':
                levels[-1].append(S[i])
                i += 1
                continue
            i += 1
            while S[i] != '}':
                if S[i] != ',':
                    levels[-1].append(S[i])
                i += 1
            i += 1

        N = len(levels)
        retSet = set()
        
        def dfs(chars):
            if len(chars) == N:
                retSet.add(''.join(chars))
                return
            for ch in levels[len(chars)]:
                chars.append(ch)
                dfs(chars)
                chars.pop()

        dfs([])                
        return list(sorted(retSet))
        