class Solution:
    def distributeCandies1(self, candies: int, num_people: int) -> List[int]:
        # slow solution
        ret = [0] * num_people
        i = 0
        prev = 0
        while candies > 0:
            cur = min(candies, prev + 1)
            ret[i] += cur
            candies -= cur
            prev = cur
            i = (i + 1) % num_people
        return ret

    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # faster solution
        # handle full assignment first
        roundIncrease = num_people * num_people
        curRound = (1 + num_people) * num_people >> 1
        rounds = 0
        while candies >= curRound:
            rounds += 1
            candies -= curRound
            curRound += roundIncrease
        ret = [(i + 1) * rounds + (rounds * (rounds - 1) * num_people >> 1)
               for i in range(num_people)]
        # handle the last round of assignment
        i = 0
        prev = rounds * num_people
        while candies > 0:
            cur = min(candies, prev + 1)
            ret[i] += cur
            candies -= cur
            prev = cur
            i += 1
        return ret
