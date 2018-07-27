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
        if(x > len(self.stack)):
            return("Not enough values in the queue to remove.")
        else:
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



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(3)
obj.push(5)
obj.push(7)
obj.push(9)
obj.pushList([7, 8, 1, 0, 65])
print("The stack is " + str(obj.stack))
obj.popList(4)
print("After removing the last 4 items, the stack is " + str(obj.stack))
obj.pop()
obj.pop()
obj.pop()
obj.pop()
param_3 = obj.top()
obj.pop()
print("The max of the stack is " + str(obj.max))
print("The min of the stack is " + str(obj.min))
param_2 = obj.pop()
param_4 = obj.empty()
