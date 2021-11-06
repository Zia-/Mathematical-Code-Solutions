import numpy as np

def get_char_count_array(str):
    count = np.zeros(256)
    for i in string:
        count[ord(i)] += 1
    return count

def first_non_repeating_char(string):
    count_array = get_char_count_array(string)
    index = -1
    k = 0
    for i in string:
        if count_array[ord(i)] == 1:
            index = k
            break
        k += 1
    return index

string = 'GeeksQuiz'
idx = first_non_repeating_char(string)
print(string[idx])

""""""

from collections import defaultdict

def areEqual(arr1, arr2):
    '''
    '''
    try:
        if (len(arr1) != len(arr2)):
            return False
        
        count = defaultdict(int)
        
        for i in arr1:
            count[i] += 1
            
        for i in arr2:
            if (count[i] == 0):
                return False
            else:
                count[i] -= 1
                
        return True
        
    except Exception as e:
        print(e)
    
if __name__ == '__main__':
    arr1 = [2,5,2,5,2]
    arr2 = [2,2,5,5,2]
    
    if (areEqual(arr1, arr2)):
        print('yes')
    else:
        print('no')

""""""



def sort_in_wave(arr):
    
    try:
        
        n = len(arr)
        
        for i in range(0, n, 2):
            
            if (i>0 and arr[i]<arr[i-1]):
                arr[i], arr[i-1] = arr[i-1], arr[i]
                # print(arr[i], )
                
            if (i<(n-1) and arr[i]<arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    arr = [10, 90, 49, 2, 1, 5, 23]
    sort_in_wave(arr)
    for i in range(0, len(arr)):
        print(arr[i])

""""""

import string

chars = string.ascii_uppercase[:26]

def getExcelStr(n):
    try:
        
        if (n <= 0):
            return 'column not defined'
        
        finalString = []
        
        while n > 0:
            remainder = n % 26
            quotient = n // 26
            
            finalString.append(chars[remainder - 1])
            
            if (remainder == 0):
                n = quotient - 1
            else:    
                n = quotient
        
        return finalString[::-1]
            
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # n = 26
    # string = getExcelStr(n)
    print(getExcelStr(26))
    print(getExcelStr(51))
    print(getExcelStr(52))
    print(getExcelStr(80))
    print(getExcelStr(676))
    print(getExcelStr(702))
    print(getExcelStr(705))

""""""



class Node:
    
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def sum(root):
    try:
        if (root == None):
            return 0
        else:
            return (sum(root.left) + root.data + sum(root.right))
        
    except Exception as e:
        print(e)
        
def is_sum_tree(root):
    try:
        if (root == None or (
            root.left == None and root.right == None
        )):
            return 1
        
        
        left_sum = sum(root.left)
        right_sum = sum(root.right)
        
        if ((root.data ==  left_sum + right_sum) and
            is_sum_tree(root.left) and is_sum_tree(root.right)
        ):
            return 1
        # else:
        return 0
        
    except Exception as e:
        print(e)
        
if __name__ == '__main__':
    
    root = Node(26)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.right = Node(3)
    
    if (is_sum_tree(root)):
        print('True')
    else:
        print('False')

""""""

def sortedInsert(s, element):
 # Base case: Either stack is empty or newly inserted
    # item is greater than top (more than all existing)
    print('b ',s, element)
    if len(s) == 0 or element > s[-1]:
        s.append(element)
        return
    else:
        # Remove the top item and recur
        temp = s.pop()
        sortedInsert(s, element)
 # Put back the top item removed earlier
        s.append(temp)
 # Method to sort stack
 
def sortStack(s):
 # If stack is not empty
    if len(s) != 0:
 # Remove the top item
        temp = s.pop()
        print('a ', temp, s)
 # Sort remaining stack
        sortStack(s)
 # Push the top item back in sorted stack
        sortedInsert(s, temp)
 # Printing contents of stack
 
def printStack(s):
    for i in s[::-1]:
        print(i, end=" ")
    print()
 # Driver Code
if __name__ == '__main__':
    s = []
    s.append(30)
    s.append(-5)
    s.append(18)
    s.append(14)
    s.append(-3)
    print("Stack elements before sorting: ")
    printStack(s)

    sortStack(s)
    # print("\nStack elements after sorting: ")
    # printStack(s)

""""""


def sortStack(s):
    try:
        for i in range(len(s)-1):
            # count = 0
            if (s[i] < s[i+1]):
                s[i], s[i+1] = s[i+1], s[i]
                # count += 1
            
        for i in range(len(s)-1):
            if (s[i] < s[i+1]):
                sortStack(s)
            
        return s
            
        
    except Exception as e:
        print(e)

# Driver Code
if __name__ == '__main__':
    s = []
    s.append(30)
    s.append(-5)
    s.append(18)
    s.append(14)
    s.append(-3)
    s.append(50)
    print("Stack elements before sorting: ")
    print(s)

    sortStack(s)
    # print("\nStack elements after sorting: ")
    print(s)

""""""

