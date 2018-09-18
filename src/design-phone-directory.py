from random import randint


class PhoneDirectory:

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.count = maxNumbers
        self.used = set()
        self.released = set()

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        num = -1
        if len(self.used) == self.count:
            return num
        if len(self.released) > 0:
            num = self.released.pop()
        else:
            while True:
                num = randint(0, self.count - 1)
                if not num in self.used:
                    break
        self.used.add(num)
        return num

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return not number in self.used

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if not number in self.used:
            return
        self.used.remove(number)
        self.released.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)

obj = PhoneDirectory(1)
ret = obj.check(0)
ret = obj.get()
ret = obj.check(0)
ret = obj.get()
