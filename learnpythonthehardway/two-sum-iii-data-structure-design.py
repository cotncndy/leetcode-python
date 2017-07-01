# Time:  O(n)
# Space: O(n)

# Design and implement a TwoSum class. It should support the following operations: add and find.
#
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
#
# For example,
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false

from collections import defaultdict

class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.__lookup = defaultdict(int)

    def add(self, number):
        self.__lookup[number] += 1


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.__lookup:
            num = value - key
            if num in self.__lookup and ( num != key or self.__lookup(num) > 1) :
                return True
        return False

if __name__ == "__main__":
    Sol = TwoSum()

    for i in (1, 3, 5):
        Sol.add(i)

    for i in (4, 7):
        print Sol.find(i)