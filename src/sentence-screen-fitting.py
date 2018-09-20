class CacheItem:
    def __init__(self, deltaR, nextC, times):
        self.deltaR = deltaR
        self.nextC = nextC
        self.times = times


class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        fullText = ' '.join(sentence) + ' '
        fullLen = len(fullText)
        offsets = [0]
        for i in range(1, fullLen):
            offsets.append(1 if fullText[i] == ' ' else offsets[i - 1] - 1)
        start = 0
        for r in range(rows):
            start += cols
            start += offsets[start % fullLen]
        return int(start / fullLen)

    def wordsTypingByCacheOfStartCol(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        totalLen = len(sentence[0])
        wordLens = [totalLen]
        for i in range(1, len(sentence)):
            totalLen += 1 + len(sentence[i])
            wordLens.append(len(sentence[i]))
        cache = dict()
        r, c = 0, 0
        si = 0
        startR, startC = 0, 0
        totalTimes = 0
        while r < rows:
            if si == 0 and c in cache:
                cacheItem = cache[c]
                if r + cacheItem.deltaR >= rows:
                    break
                totalTimes += cacheItem.times
                r += cacheItem.deltaR
                c = cacheItem.nextC
                continue
            colsLeft = cols - c
            if si == 0 and colsLeft >= totalLen:
                times = 1 + int((colsLeft - totalLen) / (totalLen + 1))
                totalTimes += times
                nextC = c + (totalLen + 1) * times
                cache[c] = CacheItem(0, nextC, times)
                c = startC = nextC
                startR = r
                continue
            if wordLens[si] > colsLeft:
                r += 1
                c = 0
                continue
            while c + wordLens[si] <= cols:
                c += wordLens[si] + 1
                if si == len(wordLens) - 1:
                    totalTimes += 1
                    cache[startC] = CacheItem(r - startR, c, 1)
                    startR = r
                    startC = c
                    si = 0
                    break
                else:
                    si += 1
        return totalTimes


sol = Solution()
#ret = sol.wordsTyping(['i', 'had', 'apple', 'pie'], 4, 5)
#ret = sol.wordsTyping(['hello', 'world'], 2, 8)
#ret = sol.wordsTyping(['f', 'p', 'a'], 8, 7)
ret = sol.wordsTyping(['a', 'bcd'], 20000, 20000)
print(ret)
