# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        return int(10 / 7 * (rand7() - 1) + 10 / 49 * (rand7() - 1) + 10 / 343 * (rand7() - 1)) + 1
