class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        weights = [0] * (limit + 1)
        for w in people:
            weights[w] += 1
        w = 1
        total = 0
        while w <= limit:
            if weights[w] > 0:
                weights[w] -= 1
                total += 1
                w1 = limit - w
                while w1 > 0 and weights[w1] == 0:
                    w1 -= 1
                if w1 > 0:
                    weights[w1] -= 1
            if weights[w] == 0:
                w += 1
        return total
    # def numRescueBoats(self, people, limit):
    #     """
    #     :type people: List[int]
    #     :type limit: int
    #     :rtype: int
    #     """
    #     people.sort(reverse=True)
    #     assigned = [False] * len(people)
    #     total = 0
    #     for i in range(len(people)):
    #         if assigned[i]:
    #             continue
    #         assigned[i] = True
    #         total += 1
    #         self.assignRemain(
    #             limit - people[i], people, assigned, i + 1, len(people) - 1)
    #     return total

    # def assignRemain(self, remain, people, assigned, begin, end):
    #     if begin == end:
    #         if people[begin] > remain:
    #             return
    #         j = begin
    #         while j < len(people) and assigned[j]:
    #             j += 1
    #         if j < len(people):
    #             assigned[j] = True
    #         return
    #     if begin > end:
    #         return
    #     mid = begin + end >> 1
    #     if people[mid] > remain:
    #         self.assignRemain(remain, people, assigned, mid + 1, end)
    #     elif mid - 1 < begin or people[mid-1] > remain:
    #         self.assignRemain(remain, people, assigned, mid, mid)
    #     else:
    #         self.assignRemain(remain, people, assigned, begin, mid - 1)


sol = Solution()
boats = sol.numRescueBoats([1, 2], 3)   # 1
boats = sol.numRescueBoats([3, 2, 2, 1], 3)  # 3
boats = sol.numRescueBoats([3, 5, 3, 4], 5)  # 4
boats = sol.numRescueBoats([5, 1, 7, 4, 2, 4], 7)   # 4
print(boats)
