"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.
more: https://www.geeksforgeeks.org/finite-automata-algorithm-for-pattern-searching/
"""

def fund_occurance(text, pat):
    """"""
    
    try:
        pat_len = len(pat)
        occurance = []
        for i in range(len(text) - pat_len):
            if text[i:i+pat_len] == pat:
                occurance.append(i)
                
        return occurance
        
    except Exception as e:
        print(e)
        
if __name__ == '__main__':
    
    text = 'AABAACAADAABAAABAA'
    pat = 'AABA'
    
    occurance_idx = fund_occurance(text, pat)

    print(occurance_idx)