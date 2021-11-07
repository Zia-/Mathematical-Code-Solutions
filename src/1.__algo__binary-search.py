"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Given a sorted array of n integers and a target value, determine if the target exisΩts in the array in logarithmic time using the binary search algorithm. If target exists in the array, print the index of it.
more: https://www.techiedelight.com/binary-search/
"""

def find_target_idx(sorted_arr, target_val, start_idx, end_idx):
    """
    Find index of target value if exists
    """
    
    try:
        
        if start_idx > end_idx:
            # We need this condition because otherwise start_idx and end_idx index will get fliped as we are performing mid_idx-1 and mid_idx+1 in each recursive call
            return -1
        
        mid_idx = (end_idx + start_idx) // 2
        
        if (sorted_arr[mid_idx] == target_val):
            return mid_idx
        
        elif (sorted_arr[mid_idx] > target_val):
            # Target is on the left of sliced array
            return find_target_idx(sorted_arr, target_val, start_idx, mid_idx-1)
            
        elif (sorted_arr[mid_idx] < target_val):
            # Target is on the right of sliced array
            return find_target_idx(sorted_arr, target_val, mid_idx+1, end_idx)                 
    except Exception as e:
        print(e)

if __name__ == '__main__':
    sorted_arr = [0, 1, 3, 5, 6, 8, 10, 12, 15]
    target_val = 3
    
    target_idx = find_target_idx(sorted_arr, target_val, 0, len(sorted_arr)-1)
    
    if (target_idx >= 0):
        print('Target value\'s index is ', target_idx)
    else:
        print('Traget does not exist')