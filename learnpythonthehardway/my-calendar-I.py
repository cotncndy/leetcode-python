class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)


class MyCalendar(object):
    def __init__(self):
        self.res = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.res:
            self.res.append(Interval(start, end))
            return True
        left, right = 0, len(self.res)
        while left < right:
            mid = left + (right - left) / 2
            if start == self.res[mid].start:
                return False
            if start < self.res[mid].start:
                right = mid
            else:
                left = mid + 1

        # print left
        if self.res and (left > 0 and self.res[left - 1].start <= start < self.res[left - 1].end or self.res[
                left - 1].start < end <
            self.res[left - 1].end) \
                or (left < len(self.res) and start <= self.res[left].start and end > self.res[left].start):
            return False
        self.res.insert(left, Interval(start, end))

        return True


if __name__ == '__main__':
    a = MyCalendar()
    # print a.book(37, 50)
    # print a.book(33, 50)
    # print a.book(4, 17)
    # print a.book(35, 48)
    # print a.book(8, 25)
    # print a.book(10, 20)
    # print a.book(15, 25)
    # print a.book(20, 30)
    print a.book(47, 50)
    print a.book(33, 41)
    print a.book(39, 45)
    print a.book(33, 42)
    print a.book(25, 32)
    print a.book(26, 35)
    print a.book(19, 25)
