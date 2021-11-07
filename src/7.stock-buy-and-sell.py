"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
The cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.
Note: There may be multiple possible solutions. Return any one of them. Any correct solution will result in an output of 1, whereas wrong solutions will result in an output of 0.
more: https://practice.geeksforgeeks.org/problems/stock-buy-and-sell-1587115621/1
"""

def stock_buying_selling_days(A):
    """
    Get when to buy or cell the stock
    """
    
    try:
        buy_idx = []
        sell_idx = []
        len_A = len(A)
        
        for i in range(len_A):
            if (i == 0):
                if (A[i] < A[i+1]):
                    buy_idx.append(i)
            elif (i == len_A-1):
                if (A[i-1] < A[i]):
                    sell_idx.append(i)
            elif (A[i-1] > A[i] and A[i] < A[i+1]):
                buy_idx.append(i)
            elif (A[i-1] < A[i] and A[i] > A[i+1]):
                sell_idx.append(i)
                
        return (buy_idx, sell_idx)
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    N = 7
    A = [100, 180, 260, 310, 40, 535, 695]
    
    print(stock_buying_selling_days(A))