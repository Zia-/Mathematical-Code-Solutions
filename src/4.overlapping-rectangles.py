"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y coordinates of two points: the left top corner and the right bottom corner of the rectangle. Two rectangles sharing a side are considered overlapping. (L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).
more: https://practice.geeksforgeeks.org/problems/overlapping-rectangles1924/1
"""

def do_they_overlap(L1, R1, L2, R2):
    """
    Overlapping rectangles
    """
    
    try:
        if (R1[0] < L2[0] or L1[0] > R2[0]):
            return False
        elif (R1[1] > L2[1] or L1[1] < R2[1]):
            return False
        else:
            return True
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # L1 = (0,10)
    # R1 = (10,0)
    # L2 = (5,5)
    # R2 = (15,0)
    
    # L1=(0,2)
    # R1=(1,1)
    # L2=(-2,2)
    # R2=(0,-3)
    
    L1=(0,2)
    R1=(1,1)
    L2=(-2,0)
    R2=(0,-3)
    
    print(do_they_overlap(L1, R1, L2, R2))