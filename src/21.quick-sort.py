"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Quick Sort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.
Given an array arr[], its starting position low and its ending position high.
Implement the partition() and quickSort() functions to sort the array.
more: https://practice.geeksforgeeks.org/problems/quick-sort/1
"""

def quick_sort(arr):
    """
    In quick sort we take first element in the array and check for all other items for greater than less than condition. Thus we have left array where all the items are less than the first iteam val and right array where all the items are greater then first item val. Return left array + first item val + right array. 
    However apply sort function to left and right array as well before returning.
    """
    
    try:
        less_than_arr = []
        equal_arr = []
        greater_than_arr = []
        
        if len(arr) > 1:
            pivot = arr[0]
            for i in range(len(arr)):
                if (arr[i] < pivot):
                    less_than_arr.append(arr[i])
                elif (arr[i] > pivot):
                     greater_than_arr.append(arr[i])
                else:
                    equal_arr.append(arr[i])
                    
            return quick_sort(less_than_arr) + equal_arr + quick_sort(greater_than_arr)
            
        else:
            return arr
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    
    N = [10, 7, 8, 9, 1, 5]

    print(quick_sort(N))