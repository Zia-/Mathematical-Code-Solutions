"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
You are given N elements and your task is to Implement a Stack in which you can get minimum element in O(1) time.
more: https://practice.geeksforgeeks.org/problems/get-minimum-element-from-stack/1
"""

class Stack:
    """
    Implement Stack
    """
    
    def __init__(self):
        self.arr = []
        return
        
    def push(self, item):
        self.arr.append(item)
        
    def pop(self):
        item = self.arr[-1]
        del self.arr[-1]
        print(item)
        return
        
    def getMin(self):
        arr = self.arr.copy()
        arr = sorted(arr)
        print(arr[0])
        return

if __name__ == '__main__':

    stack = Stack()
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.getMin()
    stack.push(1)
    stack.getMin()