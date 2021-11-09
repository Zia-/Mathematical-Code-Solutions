"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Find total number of Squares in a N*N cheesboard.
more: https://practice.geeksforgeeks.org/problems/squares-in-nn-chessboard1801/1
"""

def total_num_squares(n):
    """
    Num of squares in chessboard
    """
    
    try:
        num_of_squares = 0
        for i in range(n):
            num_of_squares += (n-i)*(n-i)
            
        return num_of_squares
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    n = 2

    print(total_num_squares(n))