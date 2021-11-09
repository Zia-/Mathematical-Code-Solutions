"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Implement a Queue using an Array. Queries in the Queue are of the following type:
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop element from queue and print the poped element)
more: https://practice.geeksforgeeks.org/problems/implement-queue-using-array/1
"""

class Queue:
    
    def __init__(self):
        self.arr = []
        return
        
    def push(self, item):
        self.arr.append(item)
        return 
        
    def pop(self):
        if (len(self.arr) == 0):
            print(-1)
            return
        item = self.arr[0]
        del self.arr[0]
        print(item)
        return
    
if __name__ == '__main__':

    queue = Queue()
    # queue.push(2)
    # queue.push(3)
    # queue.pop()
    # queue.push(4)
    # queue.pop()
    
    queue.push(3)
    queue.pop()
    queue.pop()
    queue.push(4)
    