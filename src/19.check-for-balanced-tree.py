"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Given a binary tree, find if it is height balanced or not. 
A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree. 
more: https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1
"""

class Node:
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

def height(tree):
    if tree is None:
        return 0
    height_val = max(height(tree.left), height(tree.right)) + 1
    return height_val
        
def is_balanced_tree(tree):
    try:
        if tree is None:
            return True
        
        left_sub_tree_height = height(tree.left)
        right_sub_tree_height = height(tree.right)
        
        if (abs(left_sub_tree_height - right_sub_tree_height) <= 1 and is_balanced_tree(tree.left) and is_balanced_tree(tree.right)):
            return True
        
        return False
        
    except Exception as e:
        print(e)
        
if __name__ == '__main__':
    
    # n1 = Node(1)
    # n1.left = Node(10)
    # n1.right = Node(39)
    # n1.left.left = Node(5)
    
    n1 = Node(1)
    n1.left = Node(10)
    # n1.right = Node(39)
    n1.left.left = Node(5)

    print(is_balanced_tree(n1))