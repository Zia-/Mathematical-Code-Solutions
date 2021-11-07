"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
Excel columns has a pattern like A, B, C, … ,Z, AA, AB, AC,…. ,AZ, BA, BB, … ZZ, AAA, AAB ….. etc. In other words, column 1 is named as “A”, column 2 as “B”, column 27 as “AA” and so on.
more: https://practice.geeksforgeeks.org/problems/column-name-from-a-given-column-number4244/1
"""

import string

def get_excel_cln_name(N):
    """
    Get column name from number from Excel
    """
    
    try:
        alphabet_string = string.ascii_uppercase
        cln_name_arr = []
        cln_name = ''
        
        while True:
            last_cln_idx = N // 26
            last_cln_char = alphabet_string[(N % 26) - 1]
            cln_name_arr.append(last_cln_char)
            if (last_cln_idx == 0):
                break
            N = last_cln_idx
        
        cln_name_arr_len = len(cln_name_arr)
        for i in range(cln_name_arr_len):
            cln_name += cln_name_arr[cln_name_arr_len - 1 -i]
            
        return cln_name
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    N = 13
    
    print(get_excel_cln_name(N))