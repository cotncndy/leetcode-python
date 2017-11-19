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
        i = 0
        while i < len(self.res):
            if self.res[i].start <= start < self.res[i].end or self.res[i].start < end < self.res[i].end \
                    or (start <= self.res[i].start and end >= self.res[i].end):
                return False
            if i + 1 < len(self.res) and self.res[i].end <= start and self.res[i + 1].start >= end:
                self.res = self.res[0:i + 1] + [Interval(start, end)] + self.res[i + 1:]
                return True
            i += 1

        self.res.append(Interval(start, end))

        return True


if __name__ == '__main__':
    a = MyCalendar()
    # print a.book(37, 50)
    # print a.book(33, 50)
    # print a.book(4, 17)
    # print a.book(35, 48)
    # print a.book(8, 25)
    print a.book(10, 20)
    print a.book(15, 25)
    print a.book(20, 30)
