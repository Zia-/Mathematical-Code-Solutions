"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Given an array arr[], its starting position l and its ending position r. Sort the array using merge sort algorithm.
more: https://practice.geeksforgeeks.org/problems/merge-sort/1
"""

def merge_sort(arr):
    """
    In merge sort we divide the array into two half and then we take each element one by one from both the arrays, compare them and put smaller one into the input array starting from index = 0. Do not go to the next item of a given array if its current item is still greater than the item of the other array. 
    Finally, insert remaining items of first and second array.
    """
    
    try:
        arr_len = len(arr)
        if arr_len > 1:
            
            mid_idx = arr_len // 2
            left_arr = arr[:mid_idx]
            right_arr = arr[mid_idx:]
            
            left_arr_sorted = merge_sort(left_arr)
            right_arr_sorted = merge_sort(right_arr)
            
            i = 0
            j = 0
            k = 0
            
            while i < len(left_arr_sorted) and j < len(right_arr_sorted):
                if left_arr_sorted[i] < right_arr_sorted[j]:
                    arr[k] = left_arr_sorted[i]
                    i += 1
                else:
                    arr[k] = right_arr_sorted[j]
                    j += 1
                k += 1
                
            while i < len(left_arr_sorted):
                arr[k] = left_arr_sorted[i]
                i += 1
                k += 1
                
            while j < len(right_arr_sorted):
                arr[k] = right_arr_sorted[j]
                j += 1
                k += 1
                
            return arr
            
        else:
            return arr    
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    
    N = [10, 7, 8, 9, 1, 5]

    print(merge_sort(N))