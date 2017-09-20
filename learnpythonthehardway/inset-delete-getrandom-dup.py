# Design a data structure that supports all following operations in average O(1) time.
#
# Note: Duplicate elements are allowed.
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements. The probability of each element being
# returned is linearly related to the number of same value the collection contains.
# Example:
#
# // Init an empty collection.
# RandomizedCollection collection = new RandomizedCollection();
#
# // Inserts 1 to the collection. Returns true as the collection did not contain 1.
# collection.insert(1);
#
# // Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
# collection.insert(1);
#
# // Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
# collection.insert(2);
#
# // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
# collection.getRandom();
#
# // Removes 1 from the collection, returns true. Collection now contains [1,2].
# collection.remove(1);
#
# // getRandom should return 1 and 2 both equally likely.
# collection.getRandom();

import random
import collections


class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.__map = collections.defaultdict([])
        self.__map = {}
        self.__nums = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.__nums.append(val)
        if val not in self.__map:
            self.__map[val] = [len(self.__nums) - 1]
            return True
        else:
            self.__map[val].append(len(self.__nums) - 1)
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.__map:
            return False
        idx = self.__map[val][-1]  # get the last postion of val
        self.__map[val].pop()  # remove the last index for val
        if len(self.__map[val]) == 0:  # after remove the last index, if not occur in list any more, remove it
            del self.__map[val]
        if val != self.__nums[-1]:
            self.__map[self.__nums[-1]].remove(len(self.__nums) - 1)  # bugfixed
            self.__map[self.__nums[-1]].append(idx)
            self.__nums[idx] = self.__nums[-1]  # place the last ele in list nums to the original val's position
        del self.__nums[-1]

        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.__nums[random.randint(0, len(self.__nums) - 1)]




        # Your RandomizedCollection object will be instantiated and called as such:
        # obj = RandomizedCollection()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()


if __name__ == '__main__':
    obj = RandomizedCollection()
    p1 = obj.insert(1)
    print p1
    p2 = obj.insert(1)
    print p2
    p3 = obj.insert(2)
    print p3
    print obj.insert(2)
    print obj.insert(2)
    print obj.remove(1)
    print obj.remove(1)
    print obj.remove(2)
    print obj.insert(1)
    print obj.remove(2)
    print obj.getRandom()
    print obj.getRandom()
