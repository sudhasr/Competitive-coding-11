class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #Edge Case
        if intervals == None or len(intervals) == 0:
            return False
        if len(intervals) == 1:
            return True
        count = 1
        intervals.sort()
        for i in range(1,len(intervals)):
            if intervals[i-1][1] < intervals[i][0]:
                count += 1
            else:
                return False
        if len(intervals) == count:
            return True