from collections import defaultdict


class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        if kill == 0:
            return pid
        relations = defaultdict(list)
        for i in range(len(ppid)):
            relations[ppid[i]].append(pid[i])
        ret = []
        q = [kill]
        while len(q) > 0:
            nq = []
            for p in q:
                ret.append(p)
                nq.extend(relations[p])
            q = nq
        return ret
