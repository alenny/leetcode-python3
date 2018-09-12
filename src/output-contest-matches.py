class Solution:
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        contest = [str(i) for i in range(1, n + 1)]
        while len(contest) > 1:
            nextContest = []
            full = len(contest)
            half = full >> 1
            for i in range(half):
                nextContest.append(
                    '(' + contest[i] + ',' + contest[full - i - 1] + ')')
            contest = nextContest
        return contest[0]
