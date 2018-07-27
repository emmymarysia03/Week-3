import sys

class MyQueue:
    queue = []
    min = sys.maxsize
    max = -sys.maxsize - 1

    def __init__(self):
        pass

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.queue:
            return True
        else:
            return False

    def pushList(self, x):
        self.queue = self.queue + x
        for y in range(len(x)):
            if(x[y] < self.min):
                self.min = x[y]
            elif(x[y] > self.max):
                self.max = x[y]

    def popList(self, x):
        if(x > len(self.queue)):
            return("Not enough values in the queue to remove.")
        else:
            for y in range(x):
                del self.queue[0]

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if(not(type(x) is int)):
            return("The element is not of the correct type")
        else:
            self.queue.append(x)
            if(x > self.max):
                self.max = x
            elif(x < self.min):
                self.min = x


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if(self.empty() == True):
            return("There are no elements left in your stack.")
        else:
            b = self.queue[0]
            del self.queue[0]
            return b


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if(self.empty() == True):
            return("There are no elements left in your stack.")
        else:
            b = self.queue[0]
            return b



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(3)
obj.push(5)
print(obj.push("hey"))
obj.push(9)
obj.pushList([5, 6, 1, 4])
print(obj.queue)
obj.popList(3)
print(obj.queue)
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()
print(obj.popList(3))
print(param_3)
print(param_2)
print(param_4)
