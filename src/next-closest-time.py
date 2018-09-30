class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        parts = time.split(':')
        hour = int(parts[0])
        hourHigh = int(hour / 10)
        hourLow = hour % 10
        minute = int(parts[1])
        minuteHigh = int(minute / 10)
        minuteLow = minute % 10
        digitSet = set([hourLow, hourHigh, minuteLow, minuteHigh])
        digits = list(digitSet)
        digits.sort()
        # whether minute low can be increased
        for d in digits:
            if d > minuteLow:
                return '{0:02d}:{1}{2}'.format(hour, minuteHigh, d)
        # whether minute high can be increased
        for d in digits:
            if d > 5:
                break
            if d > minuteHigh:
                return '{0:02d}:{1}{2}'.format(hour, d, digits[0])
        # whether hour low can be increased
        for d in digits:
            if d > hourLow:
                newHour = hourHigh * 10 + d
                if newHour <= 23:
                    return '{0:02d}:{1}{1}'.format(newHour, digits[0])
                break
        # whether hour high can be increased
        for d in digits:
            if d > 2:
                break
            if d > hourHigh:
                return '{0}{1}:{1}{1}'.format(d, digits[0])
        # return the earliest time of the next day
        return '{0}{0}:{0}{0}'.format(digits[0])
