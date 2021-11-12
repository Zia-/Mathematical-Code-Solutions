"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.
more: https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/1
"""

class Node:
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

def b_2_dll(n):
    """"""
    
    try:
        if n is None:
            return
        
        left_node = n.left
        right_node = n.right
        
        arr = []
        if left_node is not None:
            left_item = b_2_dll(left_node)
            arr += left_item
            
        arr += [n.item]
        
        if right_node is not None:
            right_item = b_2_dll(right_node)
            arr += right_item
        
        return arr
        
    except Exception as e:
        print(e)
        
if __name__ == '__main__':
    
    # n = Node(10)
    # n.left = Node(12)
    # n.left.left = Node(25)
    # n.left.right = Node(30)
    # n.right = Node(15)
    # n.right.left = Node(36)
    
    n = Node(10)
    n.left = Node(20)
    n.left.left = Node(40)
    n.left.right = Node(60)
    n.right = Node(30)
    # n.right.left = Node(36)

    print(b_2_dll(n))