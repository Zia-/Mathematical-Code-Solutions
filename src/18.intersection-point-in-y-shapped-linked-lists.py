"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Given two singly linked lists of size N and M, write a program to get the point where two linked lists intersect each other.
more: https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1
"""

class Node:
    def __init__(self, item, next = None):
        self.item = item
        self.next = next

def linked_node(n1, n2):
    try:
        pointer_list = []
        
        while(n1 != None):
            pointer_list.append(id(n1))
            n1 = n1.next
        while(n2 != None):
            if (id(n2) in pointer_list):
                return n2.item
            n2 = n2.next
            
        return -1
        
    except Exception as e:
        print(e)
        
if __name__ == '__main__':
    
    n1 = Node(1)
    n1.next = Node(2)
    n1.next.next = Node(3)
    n1.next.next.next = Node(4)
    n1.next.next.next.next = Node(5)
    n1.next.next.next.next.next = Node(6)
    n1.next.next.next.next.next.next = Node(7)
    
    n2 = Node(10)
    n2.next = Node(9)
    n2.next.next = Node(8)
    n2.next.next.next = n1.next.next.next

    print(linked_node(n1, n2))