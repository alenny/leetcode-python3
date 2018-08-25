# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda itm: itm.start)
        prevEnd = 0
        for interval in intervals:
            if interval.start < prevEnd:
                return False
            prevEnd = interval.end
        return True
