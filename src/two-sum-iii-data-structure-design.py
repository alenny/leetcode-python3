from collections import defaultdict


class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__dataMap = defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.__dataMap[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for number in self.__dataMap.keys():
            n2 = value - number
            if n2 == number and self.__dataMap[number] > 1 or n2 != number and n2 in self.__dataMap:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
