from typing import List
from collections import defaultdict


class Excel:

    def __init__(self, H: int, W: str):
        self.OrdA = ord('A')
        self.Rows = H
        self.Cols = ord(W) - self.OrdA + 1
        self.values = [[0] * self.Cols for _ in range(self.Rows)]
        self.formulas = defaultdict(dict)

    def set(self, r: int, c: str, v: int) -> None:
        cr, cc = self.__r(r), self.__c(c)
        if (cr, cc) in self.formulas:
            self.formulas.pop((cr, cc))
        self.__set(cr, cc, v)

    def get(self, r: int, c: str) -> int:
        return self.__get(self.__r(r), self.__c(c))

    def sum(self, r: int, c: str, strs: List[str]) -> int:
        cr, cc = self.__r(r), self.__c(c)
        ret = 0
        formula = dict()
        for s in strs:
            parts = s.split(':')
            pr0, pc0 = self.__r(int(parts[0][1:])), self.__c(parts[0][0])
            if len(parts) == 1:
                ret += self.__get(pr0, pc0)
                self.__addToFormula(formula, pr0, pc0)
            else:
                pr1, pc1 = self.__r(int(parts[1][1:])), self.__c(parts[1][0])
                for pr in range(pr0, pr1 + 1):
                    for pc in range(pc0, pc1 + 1):
                        ret += self.__get(pr, pc)
                        self.__addToFormula(formula, pr, pc)
        self.formulas[(cr, cc)] = formula
        self.__set(cr, cc, ret)
        return ret

    def __r(self, r: int) -> int:
        return r - 1

    def __c(self, c: str) -> int:
        return ord(c) - self.OrdA

    def __get(self, cr: int, cc: int) -> int:
        return self.values[cr][cc]

    def __set(self, cr: int, cc: int, v: int):
        diff = v - self.values[cr][cc]
        self.values[cr][cc] = v
        for (fr, fc), formula in self.formulas.items():
            if not (cr, cc) in formula:
                continue
            self.__set(fr, fc, self.values[fr][fc] + diff * formula[(cr, cc)])

    def __addToFormula(self, formula: dict, cr, cc):
        if (cr, cc) in formula:
            formula[(cr, cc)] += 1
        else:
            formula[(cr, cc)] = 1

# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)


obj = Excel(3, "C")
ret = obj.sum(1, "A", ['A2'])
print(ret)
obj.set(2, 'A', 1)
ret = obj.get(1, "A")
print(ret)
