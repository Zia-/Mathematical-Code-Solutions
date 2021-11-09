"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array and return it
In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....
more: https://practice.geeksforgeeks.org/problems/wave-array-1587115621/1
"""

def wave_arr(n):
    """
    Generate wave array
    """
    
    try:
        mid_idx = len(n) // 2
        
        for i in range(mid_idx):
            if (n[2*i] < n[2*i+1]):
                n[2*i], n[2*i+1] = n[2*i+1], n[2*i]
                
        return n
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # n = [1,2,3,4,5]
    n = [2,4,7,8,9,10]

    print(wave_arr(n))