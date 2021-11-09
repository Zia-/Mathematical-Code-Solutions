"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
A linked list class
more: ...
"""

class Node:
    """
    """
    
    def __init__(self, item = None, next = None):
        self.item = item
        # next is an internal method to link to another obj
        self.next = next
        return
    
class LinkedList:
    """
    """
    
    def __init__(self):
        self.head = None
        
    def insert(self, item):
        new_node = Node(item)
        if(self.head):
            current_node = self.head
            # next method is being called to check if any child node exists or not. If not then assign newly provided node as terminating child.
            while(current_node.next):
                current_node = current_node.next
            current_node.next = new_node
        else:
            self.head = new_node
    
    def print_ll(self):
        current_node = self.head
        while(current_node):
            print(current_node.item)
            current_node = current_node.next
    
    
if __name__ == '__main__':

    ll = LinkedList()
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.print_ll()
    