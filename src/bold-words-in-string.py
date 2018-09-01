class Solution:
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        ws = set(words)
        ranges = []
        left, right = 0, 0
        while left < len(S) and right < len(S):
            oldRight = right
            rightest = -1
            while right < len(S):
                if S[left:right + 1] in ws:
                    rightest = right
                right += 1
            if rightest == -1:
                left += 1
                right = max(left, oldRight)
                continue
            if len(ranges) == 0 or ranges[-1][1] < left - 1:
                ranges.append([left, rightest])
            else:
                ranges[-1][1] = rightest
            left += 1
            right = rightest + 1
        if len(ranges) == 0:
            return S
        ret = ''
        begin = 0
        for rg in ranges:
            ret += S[begin:rg[0]] + '<b>' + S[rg[0]:rg[1] + 1] + '</b>'
            begin = rg[1] + 1
        ret += S[ranges[-1][1] + 1:]
        return ret


sol = Solution()
#ret = sol.boldWords(["ccb", "b", "d", "cba", "dc"], "eeaadadadc")
ret = sol.boldWords(["di","r","buhozb","lofjmyjj","qagllw","zzuid","loyugfh","w","hcfg","ttd","vjqigvx","u","mhbivve","x","nzbvyfzx","zs","j","zgtud","zm","huevyex","szwigrlwzm","vlrjmobu","b","h","gcmdgyv","anyfelm","vtcejv","myjjzn","jznnj","awcxmjn","lw","sju","szszwigrl","eze","ffikvecua","bklrhsju","gyazwel","pdhnsxsod","zn","rhsjus","zk","gctgu","vzndt","mfd","jlws","j","zxgaudyo","apa","znvixpdh","tgubzczgt"], "wwcyuaqzgtudmpjkluqoseslygywzkixjqghsocvjqigvxwqloyugfhcjscjghqmiglgyazwelshzapaezqgmcmrmfrfzttdgquizyducbvxzzuiddcnwuaapdunzlbagnifndbjyalqqgbramhbivvervxrtcszszwigrlwzmuteyswzagudtpvlrjmobuhozbghkhvoxawcxmjnazlqlkqqqnoclufgkovbokvkoezeknwhcfgcenvaablpvtcejvzndtzncrelhedwlwiqgdbdgctgubzczgtovufncicjlwsmfdcrqeaghuevyexqdhffikvecuazrelofjmyjjznnjdkimbklrhsjusbstqhvlejtjcczqnzbvyfzxgaudyosckysmminoanjmbafhtnbrrzqagllwxlxmjanyfelmwruftlzuuhbsjexoobjkmymlitiwjtdxscotzvznvixpdhnsxsodieatipiaodgcmdgyv")
