import sys

class MyStack:
    stack = []
    min = sys.maxsize
    max = -sys.maxsize - 1

    def __init__(self):
        """
        Initialize your data structure here.
        """
        pass
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if not self.stack:
            return True
        else:
            return False


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if(not(type(x) is int)):
            return("The element is not of the correct type")
        else:
            self.stack.append(x)
            if(x > self.max):
                self.max = x
            elif(x < self.min):
                self.min = x

    def pushList(self, x):
        self.stack = self.stack + x
        for y in range(len(x)):
            if(x[y] < self.min):
                self.min = x[y]
            elif(x[y] > self.max):
                self.max = x[y]

    def popList(self, x):
        for y in range(x):
            l = len(self.stack)
            del self.stack[l - 1]

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if(self.empty() == True):
            return("There are no elements left in your stack.")
        else:
            l = len(self.stack)
            a = self.stack[l - 1]
            del self.stack[l - 1]
            return a


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        l = len(self.stack)
        return self.stack[l - 1]

class MyQueue:

    s1 = MyStack()
    s2 = MyStack()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        pass

    def s1tos2(self):
        for x in range(len(s1)):
            s2.push(s1[0])
            

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
