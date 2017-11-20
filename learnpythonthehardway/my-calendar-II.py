# Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a
#  triple booking.
#
# Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open
# interval [start, end), the range of real numbers x such that start <= x < end.
#
# A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common
#  to all 3 events.)
#
# For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully
# without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
#
# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
# Example 1:
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(50, 60); // returns true
# MyCalendar.book(10, 40); // returns true
# MyCalendar.book(5, 15); // returns false
# MyCalendar.book(5, 10); // returns true
# MyCalendar.book(25, 55); // returns true
# Explanation:
# The first two events can be booked.  The third event can be double booked.
# The fourth event (5, 15) can't be booked, because it would result in a triple booking.
# The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
# The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
# the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
# Note:
#
# The number of calls to MyCalendar.book per test case will be at most 1000.
# In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].


class MyCalendarTwo(object):
    def __init__(self):
        self.res = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool

        """

        left, right = 0, len(self.res)
        while left < right:
            mid = left + (right - left) / 2
            if start == self.res[mid][0]:
                left = mid
                break
            if start > self.res[mid][0]:
                left = mid + 1
            else:
                right = mid

        if left == len(self.res):
            self.res.append((start, end))
            return True

        l = left
        while l and self.res[l][1] >= start:
            l -= 1
        if self.res[l][1] < start:
            l += 1

        r = left
        while r < len(self.res) and self.res[r][0] < end:
            r += 1
        for i in xrange(l, r):
            for j in xrange(i + 1, r):
                intersect = self.interRange(self.res[i], self.res[j])
                if self.interRange((start, end), intersect) is not None:
                    return False

        self.res.insert(left, (start, end))
        return True

    def interRange(self, range1, range2):
        if range1 is None or range2 is None:
            return None
        if range1[1] <= range2[0] or range2[1] <= range1[0]:
            return None
        return (max(range1[0], range2[0]), min(range1[1], range2[1]))


if __name__ == '__main__':
    a = MyCalendarTwo()
    print a.book(24, 40)
    print a.book(43, 50)
    print a.book(27, 43)
    print a.book(5, 21)
    print a.book(30, 40)
    print a.book(14, 29)
    print a.book(3, 19)
    print a.book(3, 14)





    # Your MyCalendarTwo object will be instantiated and called as such:
    # obj = MyCalendarTwo()
    # param_1 = obj.book(start,end)
