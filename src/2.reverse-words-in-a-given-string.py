"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Given a String S, reverse the string without reversing its individual words. Words are separated by dots.
more: https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1
"""

def reverse_string(S):
    """
    Reverse string
    """
    
    try:

        S_arr = []
        string_len = len(S)
        single_word = ''
        
        # Get individual words into array
        for i in range(string_len):
            if (S[i] == '.' and len(single_word) > 0):
                S_arr.append(single_word)
                single_word = ''
            elif (i == string_len-1 and len(single_word) > 0):
                single_word += S[i]
                S_arr.append(single_word)
            elif (S[i] != '.'):
                single_word += S[i] 
        
        S_arr_len = len(S_arr)
        S_reversed = ''
        # Remake string with reversed words inserting dot in between each word
        for i in range(S_arr_len):
            if (i > 0):
                S_reversed += '.'
            S_reversed += S_arr[S_arr_len -1 -i]
        
        # Check if original string had starting or ending dots
        if (S[string_len - 1] == '.'):
            S_reversed = '.' + S_reversed
        if (S[0] == '.'):
            S_reversed = S_reversed + '.'
        
        return S_reversed
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    S = '.i.like.this.program.very.much.'
    # S = 'i.like.this.program.very.much.'
    # S = 'i.like.this.program.very.much'
    # S = '..i.like.this...program.very.much.' # Fails, only considers one dot
        
    print(reverse_string(S))