"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Find HCF
more: 
"""
        
def find_hcf(a, b):
    try:
        a_factor = []
        int_count = 1
        while True:
            if a % int_count == 0:
                a_factor.append(int_count)
            if int_count == a:
                break
            int_count += 1
            
        b_factor = []
        int_count = 1
        while True:
            if b % int_count == 0:
                b_factor.append(int_count)
            if int_count == b:
                break
            int_count += 1
            
        len_a_factor = len(a_factor)
        for i in range(len_a_factor):
            rev_a_factor = a_factor[len_a_factor - 1 - i]
            if rev_a_factor in b_factor:
                return rev_a_factor
        
    except Exception as e:
        print(e)
        
if __name__ == '__main__':

    print(find_hcf(8, 20))