"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Given a string S consisting of lowercase Latin Letters. Find the first non-repeating character in S.
more: https://practice.geeksforgeeks.org/problems/non-repeating-character-1587115620/1
"""

def first_non_repeating_char(S):
    """
    Non repeating character
    """
    
    try:
        
        hash_map = {}
        
        for i in S:
            if (i not in hash_map):
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        
        for i in S:
            if (hash_map[i] == 1):
                return i
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    S = 'zxvczbtxyzvy'
    
    print(first_non_repeating_char(S))