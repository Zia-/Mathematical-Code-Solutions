"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Find total number of Rectangles (excluding squares) in a N*N chessboard.
more: https://practice.geeksforgeeks.org/problems/rectangles-in-nn-board5930/1
"""

def total_num_rectangles(n):
    """
    Num of rectangles in chessboard
    """
    
    try:
        num_of_squares = 0
        for i in range(n):
            # total num of squares in a chessboard 1*1+2*2+3*3...
            num_of_squares += (i+1)*(i+1)
            
        total_num_of_sq_rec = 0
        for i in range(n):
            # total num of squares+rectangles in a chessboard 1*1*1+2*2*2+3*3*3...
            total_num_of_sq_rec += (i+1)*(i+1)*(i+1)
            
        return total_num_of_sq_rec - num_of_squares
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    n = 2

    print(total_num_rectangles(n))