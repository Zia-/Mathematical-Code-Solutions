"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
You are given a pointer/ reference to the node which is to be deleted from the linked list of N nodes. The task is to delete the node. Pointer/ reference to head node is not given. 
Note: No head reference is given to you. It is guaranteed that the node to be deleted is not a tail node in the linked list.
more: https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1
"""

class Node:
    def __init__(self, item, next = None):
        self.item = item
        self.next = next

def delete_node(n1, node):
    """"""
    
    try:
        if n1 is None:
            return     
        
        if node != n1.item:
            # note not to alter preceding nodes
            delete_node(n1.next, node)
        else:
            # only alter node that matches given int value and subsequently tailing nodes
            n1.item, n1.next = n1.next.item, n1.next.next
        
        return n1
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    
    n1 = Node(10)
    n1.next = Node(20)
    n1.next.next = Node(4)
    n1.next.next.next = Node(30)
    
    # n1 = Node(1)
    # n1.left = Node(10)
    # n1.right = Node(39)
    new_n1 = delete_node(n1, 20)

    print(new_n1.item, new_n1.next.item, new_n1.next.next.item)