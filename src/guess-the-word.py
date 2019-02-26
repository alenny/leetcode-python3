# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """


class Master:
    def __init__(self, target):
        self.target = target

    def guess(self, word):
        matches = 0
        for ci in range(6):
            if word[ci] == self.target[ci]:
                matches += 1
        return matches


from random import randint


class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        N = len(wordlist)
        possibleIndexes = set([i for i in range(N)])
        times = 0
        while True:
            times += 1
            idx = self.__pickOne(possibleIndexes, N)
            matches = master.guess(wordlist[idx])
            if matches == 6:
                break
            self.__filter(wordlist, idx, possibleIndexes, matches)
        return times

    def __pickOne(self, possibleIndexes, N):
        while True:
            idx = randint(0, N - 1)
            if idx in possibleIndexes:
                possibleIndexes.remove(idx)
                return idx
        return None

    def __filter(self, wordlist, refIdx, possibleIndexes, matches):
        word = wordlist[refIdx]
        indexesToRemove = set()
        for i in possibleIndexes:
            w = wordlist[i]
            m = 0
            for ci in range(6):
                if w[ci] != word[ci]:
                    continue
                m += 1
                if m >= matches:
                    break
            if m < matches:
                indexesToRemove.add(i)
        possibleIndexes.difference_update(indexesToRemove)

target = "hbaczn"
lst = ["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"]
master = Master(target)
sol = Solution()
ret = sol.findSecretWord(lst, master)
print(ret)