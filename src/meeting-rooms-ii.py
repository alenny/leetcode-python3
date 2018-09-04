# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda i: i.start)
        rooms = []
        for meeting in intervals:
            availableRoomIdx = -1
            for i in range(len(rooms)):
                if rooms[i] <= meeting.start:
                    availableRoomIdx = i
                    break
            if availableRoomIdx == -1:
                rooms.append(meeting.end)
            else:
                rooms[availableRoomIdx] = meeting.end
        return len(rooms)


sol = Solution()
ret = sol.minMeetingRooms([Interval(7, 10), Interval(2, 4)])
