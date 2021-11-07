"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Given three integers x, y, and z, the task is to find the sum of all the numbers formed by 
having 4 at most x times, having 5 at most y times, and having 6 at most z times as a digit.
more: https://practice.geeksforgeeks.org/problems/number-formation3506/1
"""

from collections import Counter

def number_formation(x4, y5, z6):
    """
    Number formation
    """
    
    try:
        
        if (x4 == y5 == z6 == 0):
            return 0
        
        # get largest possible int
        largest_number = ''
        for i in range(z6):
            largest_number += '6'
        for i in range(y5):
            largest_number += '5'
        for i in range(x4):
            largest_number += '4'
        
        largest_number_str_arr = list(largest_number)
        # find all numbers that makes up of repeating 4, 5 and 6. Main catch is the use of Counter.
        possible_numbers = []
        for i in range(int(largest_number)+1):
            int_str = str(i)
            int_str_arr = list(int_str)
            diff = list((Counter(int_str_arr) - Counter(largest_number_str_arr)).elements())
            if (len(diff) == 0):
                possible_numbers.append(int_str)

        sum = 0
        for i in possible_numbers:
            sum += int(i)
            
        return sum
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    x4 = 1
    y5 = 1
    z6 = 1
    
    print(number_formation(x4, y5, z6))