# Design and implement a data structure for a compressed string iterator. It should support the following operations:
#  next and hasNext.
#
# The given compressed string will be in the form of each letter followed by a positive integer representing the
# number of this letter existing in the original uncompressed string.
#
# next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white
#  space.
# hasNext() - Judge whether there is any letter needs to be uncompressed.
#
# Note:
# Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted
# across multiple test cases. Please see here for more details.
#
# Example:
#
# StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
#
# iterator.next(); // return 'L'
# iterator.next(); // return 'e'
# iterator.next(); // return 'e'
# iterator.next(); // return 't'
# iterator.next(); // return 'C'
# iterator.next(); // return 'o'
# iterator.next(); // return 'd'
# iterator.hasNext(); // return true
# iterator.next(); // return 'e'
# iterator.hasNext(); // return false
# iterator.next(); // return ' '


class StringIterator(object):
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.pos, self.count, self.leng = 0, 0, len(compressedString)
        self.st = compressedString

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            self.count -= 1
            return self.ch

        return ' '

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.count == 0 and self.pos < self.leng:
            self.ch = self.st[self.pos]
            self.pos += 1
            while self.pos < self.leng and self.st[self.pos].isdigit():  # bugfixed
                self.count = self.count * 10 + ord(self.st[self.pos]) - ord('0')
                self.pos += 1

        return self.count != 0


# fastest one among python solution, 58ms.
class StringIterator2(object):
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.i = 0
        self.count = 0
        self.c = None
        self.str = compressedString

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext() is False:
            return " "
        if self.count == 0:
            self.c = self.str[self.i]  # get character
            self.count = 0  # how many characters
            self.i += 1  # move to next index
            # calculate total number of characteris
            while self.i < len(self.str) and ord(self.str[self.i]) <= ord('9') and ord(self.str[self.i]) >= ord('0'):
                self.count = self.count * 10 + ord(self.str[self.i]) - ord("0")
                self.i = self.i + 1

        self.count -= 1
        return self.c

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.count > 0 or self.i < len(self.str)




        # Your StringIterator object will be instantiated and called as such:
        # obj = StringIterator(compressedString)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()


if __name__ == '__main__':
    st = StringIterator("L1e2t1C1o1d1e1")
    while st.hasNext():
        print st.next()
