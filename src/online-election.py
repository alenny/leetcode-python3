from collections import defaultdict


class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.leadings = [(times[0], persons[0])]
        self.votes = defaultdict(int)
        for i in range(len(persons)):
            self.votes[persons[i]] += 1
            if self.leadings[-1][1] != persons[i] and \
                    self.votes[persons[i]] >= self.votes[self.leadings[-1][1]]:
                self.leadings.append((times[i], persons[i]))

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        begin = 0
        end = len(self.leadings) - 1
        while begin <= end:
            mid = begin + end >> 1
            if self.leadings[mid][0] > t:
                end = mid - 1
            else:
                begin = mid + 1
        return self.leadings[begin - 1][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

sol = TopVotedCandidate([0, 1, 0, 1, 1], [24, 29, 31, 76, 81])
ret = sol.q(29)
