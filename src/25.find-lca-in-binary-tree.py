"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Find LCA - Lowest Common Ancestor (LCA) of two nodes u and v in a rooted tree T is defined as the node located farthest from the root that has both u and v as descendants.
more: https://www.geeksforgeeks.org/find-lca-in-binary-tree-using-rmq/
"""

class Node:
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

def get_root(t, arr, n):
    try:
        if t is None:
            return False
        
        arr += [t.item]
        
        if t.item == n:
            return True
        
        if (get_root(t.left, arr, n) or get_root(t.right, arr, n)):
            return True
        
        del arr[-1]
        return False
        
    except Exception as e:
        print(e)
        
def find_lca(t, a, b):
    try:
        if t is None:
            return
        
        a_root = []
        b_root = []
        get_root(t, a_root, a)
        get_root(t, b_root, b)
        
        len_a_root = len(a_root)
        
        for i in range(len_a_root):
            rev_i = a_root[len_a_root - 1 -i]
            if rev_i in b_root:
                return rev_i
            
        return -1
        
    except Exception as e:
        print(e)
        
if __name__ == '__main__':
    
    t = Node(1)
    t.left = Node(2)
    t.left.left = Node(4)
    t.left.right = Node(5)
    t.left.right.left = Node(8)
    t.left.right.right = Node(9)
    t.right = Node(3)
    t.right.left = Node(6)
    t.right.right = Node(7)

    print(find_lca(t, 4, 9))