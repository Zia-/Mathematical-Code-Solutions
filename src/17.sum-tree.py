"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Given a Binary Tree. Return 1 if, for every node X in the tree other than the leaves, its value is equal to the sum of its left subtree's value and its right subtree's value. Else return 0.
An empty tree is also a Sum Tree as the sum of an empty tree can be considered to be 0. A leaf node is also considered a Sum Tree.
more: https://practice.geeksforgeeks.org/problems/sum-tree/1
"""

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

def get_height(root):
    try:
        if root is None:
            return 0
        height = root.item + get_height(root.left) + get_height(root.right)
        return height
        
    except Exception as e:
        print(e)

def is_balanced(tree):
    try:
        if tree is None:
            return 1
        if tree.left == None and tree.right == None:
            return 1
        
        left_height = get_height(tree.left)
        right_height = get_height(tree.right)
        
        print(left_height, right_height, tree.item)
        
        if (tree.item == left_height + right_height and is_balanced(tree.left) and is_balanced(tree.right)):
            return 1
        else:
            return 0
        
    except Exception as e:
        print(e)
    
if __name__ == '__main__':

    root = Node(3)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(10)
    root.left.right = Node(10)
    # root.left.left.left = Node(8)
    
    print(is_balanced(root))