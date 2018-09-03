from collections import defaultdict


class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        groups = [words]
        pos = 0
        dep = defaultdict(set)
        letterSet = set()
        for word in words:
            for i in range(len(word)):
                letterSet.add(word[i])
        while len(groups) > 0:
            nextGroups = []
            for group in groups:
                prevWord = ''
                for word in group:
                    if prevWord != '' and prevWord[pos] != word[pos]:
                        dep[word[pos]].add(prevWord[pos])
                    if prevWord == '' or prevWord[pos] != word[pos]:
                        if len(nextGroups) > 0 and len(nextGroups[-1]) < 2:
                            nextGroups.pop()
                        if len(word) > pos + 1:
                            nextGroups.append([word])
                    elif len(word) > pos + 1:
                        if len(nextGroups) > 0:
                            nextGroups[-1].append(word)
                        else:
                            nextGroups.append([word])
                    prevWord = word
            if len(nextGroups) > 0 and len(nextGroups[-1]) < 2:
                nextGroups.pop()
            groups = nextGroups
            pos += 1
        if len(letterSet) == 1:
            return words[0]
        ret = ''
        while len(letterSet) > 0:
            letterNoDep = ''
            for letter in letterSet:
                if not letter in dep:
                    letterNoDep = letter
                    break
            if letterNoDep == '':
                return ''
            ret += letterNoDep
            letterSet.remove(letterNoDep)
            depItems = list(dep.items())
            for k, v in depItems:
                if not letterNoDep in v:
                    continue
                v.remove(letterNoDep)
                if len(v) == 0:
                    dep.pop(k)
        return ret


sol = Solution()
#ret = sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
#ret = sol.alienOrder(["wrt", "wrtkj"])
ret = sol.alienOrder(["ab", "adc"])
