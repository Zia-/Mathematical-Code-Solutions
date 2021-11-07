"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included. Write a program to find Nth Ugly Number.
more: https://practice.geeksforgeeks.org/problems/ugly-numbers2254/1
"""

def find_nth_ugly_number(N):
    """
    Ugly numbers
    """
    
    try:
        ugly_num_idx = 1
        nth_ugly_num = 1
        count_int = 1
        
        while True:
            
            # keep checking if the number is divisible by 2, 3 or 5 and keep using quotient until you hit 1. Increment counters and numbers accordingly and simply increment the number being tested if it is not divible by 2, 3 or 5 in the final else block. 
            if (count_int % 2 == 0):
                count_int = count_int // 2
            elif (count_int % 3 == 0):
                count_int = count_int // 3
            elif (count_int % 5 == 0):
                count_int = count_int // 5
            elif (count_int == 1):
                if (ugly_num_idx == N):
                    break
                ugly_num_idx += 1
                nth_ugly_num += 1
                count_int = nth_ugly_num
            else:
                nth_ugly_num += 1
                count_int = nth_ugly_num
            
        return nth_ugly_num
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    N = 11
    
    print(find_nth_ugly_number(N))