class Solution:
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.matchHelper(pattern, str, 0, 0, dict(), set())

    def matchHelper(self, pattern, string, pi, si, dictionary, matched):
        if pi == len(pattern) and si == len(string):
            return True
        if pi < len(pattern) and si >= len(string) or \
                pi >= len(pattern) and si < len(string):
            return False
        key = pattern[pi]
        if key in dictionary:
            target = dictionary[key]
            return string.startswith(target, si) and \
                self.matchHelper(pattern, string, pi + 1,
                                 si + len(target), dictionary, matched)
        # not key in dictionary
        end = si + 1
        while end <= len(string):
            target = string[si:end]
            if target in matched:
                end += 1
                continue
            dictionary[key] = target
            matched.add(target)
            if self.matchHelper(pattern, string, pi + 1, end, dictionary, matched):
                return True
            dictionary.pop(key)
            matched.remove(target)
            end += 1
        return False


sol = Solution()
ret = sol.wordPatternMatch("aabb", "xyzabcxzyabc")
print(ret)
