# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        free = [Interval(-1, pow(10, 8) + 1)]
        for sch in schedule:
            newFree = []
            fi, si = 0, 0
            while fi < len(free) and si < len(sch):
                if free[fi].end <= sch[si].start:
                    newFree.append(free[fi])
                    fi += 1
                elif sch[si].end <= free[fi].start:
                    si += 1
                else:
                    if free[fi].start < sch[si].start:
                        newFree.append(Interval(free[fi].start, sch[si].start))
                    if free[fi].end < sch[si].end:
                        fi += 1
                    elif free[fi].end == sch[si].end:
                        fi += 1
                        si += 1
                    else:
                        # free[fi].end > sch[si].end:
                        free[fi].start = sch[si].end
                        si += 1
            while fi < len(free):
                newFree.append(free[fi])
                fi += 1
            free = newFree
        return free[1:-1]

    def employeeFreeTimeByUnionFirst(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        union = schedule[0]
        for i in range(1, len(schedule)):
            sch = schedule[i]
            newUnion = []
            ui, si = 0, 0
            while ui < len(union) and si < len(sch):
                if union[ui].end < sch[si].start:
                    self.putInterval(newUnion, union[ui].start, union[ui].end)
                    ui += 1
                elif sch[si].end < union[ui].start:
                    self.putInterval(newUnion, sch[si].start, sch[si].end)
                    si += 1
                else:
                    joinStart = min(union[ui].start, sch[si].start)
                    joinEnd = max(union[ui].end, sch[si].end)
                    self.putInterval(newUnion, joinStart, joinEnd)
                    ui += 1
                    si += 1
            while ui < len(union):
                self.putInterval(newUnion, union[ui].start, union[ui].end)
                ui += 1
            while si < len(sch):
                self.putInterval(newUnion, sch[si].start, sch[si].end)
                si += 1
            union = newUnion
        # find the free time intervals
        ret = []
        for i in range(0, len(union) - 1):
            ret.append(Interval(union[i].end, union[i + 1].start))
        return ret

    def putInterval(self, union, start, end):
        if len(union) == 0 or union[-1].end < start:
            union.append(Interval(start, end))
        else:
            union[-1].end = max(union[-1].end, end)


sol = Solution()
# inp = [[[7,24],[29,33],[45,57],[66,69],[94,99]],[[6,24],[43,49],[56,59],[61,75],[80,81]],[[5,16],[18,26],[33,36],[39,57],[65,74]],[[9,16],[27,35],[40,55],[68,71],[78,81]],[[0,25],[29,31],[40,47],[57,87],[91,94]]]
inp = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
args = []
for lst in inp:
    sch = []
    for start, end in lst:
        sch.append(Interval(start, end))
    args.append(sch)
ret = sol.employeeFreeTime(args)
