"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order without using any extra space. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.
more: https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
"""

def merge_two_arr(n, m, arr1, arr2):
    """
    Merge arrays without extra space
    """
    
    try:
        i = n-1
        j = 0
        while i >= 0 and j < m :
            if arr1[i] > arr2[j]:
                arr1[i],arr2[j] = arr2[j],arr1[i]
            i -= 1
            j += 1
        arr1.sort()
        arr2.sort()
        
        return (arr1, arr2)        
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    n = 5
    m = 4
    arr2 = [1,3,5,7]
    arr1 = [0,2,6,8,9]
    
    print(merge_two_arr(n, m, arr1, arr2))