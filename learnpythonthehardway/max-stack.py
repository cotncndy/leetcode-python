# Design a max stack that supports push, pop, top, peekMax and popMax.
#
# push(x) -- Push element x onto stack.
# pop() -- Remove the element on top of the stack and return it.
# top() -- Get the element on the top.
# peekMax() -- Retrieve the maximum element in the stack.
# popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements,
# only remove the top-most one.
# Example 1:
# MaxStack stack = new MaxStack();
# stack.push(1);
# stack.push(5);
# stack.push(5);
# stack.top(); -> 5
# stack.popMax(); -> 5
# stack.top(); -> 1
# stack.peekMax(); -> 5
# stack.pop(); -> 1
# stack.top(); -> 5
# Note:
# -1e7 <= x <= 1e7
# Number of operations won't exceed 10000.
# The last four operations won't be called when stack is empty.

class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack, self.__maxStack = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.__stack.append(x)
        if not self.__maxStack or x >= self.__maxStack[-1]:
            self.__maxStack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        x = self.__stack.pop()
        if x == self.__maxStack[-1]:
            self.__maxStack.pop()
        return x


    def top(self):
        """
        :rtype: int
        """
        return self.__stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.__maxStack[-1]

    def popMax(self):
        """
        :rtype: int
        """
        temp = []
        while self.__stack[-1] < self.peekMax():
            temp.append(self.__stack.pop())
        # find the max
        x = self.__maxStack.pop()
        self.__stack.pop()

        while temp:
            self.push(temp.pop())
        return x

if __name__ == '__main__':
    stack = MaxStack()
    stack.push(5)
    stack.push(1)
    stack.push(5)
    print stack.top()
    print stack.popMax()
    print stack.top()
    print stack.peekMax()
    print stack.pop()
    print stack.top()

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
