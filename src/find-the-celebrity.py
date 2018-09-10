# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
#    def knows(a, b):
#        return True


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        notKnown = [set() for i in range(n)]
        possible = [True for i in range(n)]
        for b in range(n):
            if not possible[b]:
                continue
            for a in range(n):
                if a == b:
                    continue
                if not knows(a, b):
                    possible[b] = False
                    notKnown[a].add(b)
                    break
                else:
                    possible[a] = False
        for a in range(n):
            if not possible[a]:
                continue
            aKnowsSomeone = False
            for b in range(n):
                if b == a or b in notKnown[a]:
                    continue
                if knows(a, b):
                    aKnowsSomeone = True
                    break
            if not aKnowsSomeone:
                return a
        return -1
