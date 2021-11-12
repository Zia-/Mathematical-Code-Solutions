"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Find LCM
more: 
"""
        
def find_lcm(a, b):
    try:
        a_ori = a
        b_ori = b
        
        while True:
            if a == b:
                break
            elif a < b:
                a += a_ori
            else:
                b += b_ori
                                
        return a
        
    except Exception as e:
        print(e)
        
if __name__ == '__main__':

    print(find_lcm(8, 15))