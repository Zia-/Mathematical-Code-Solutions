"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Design a data structure that works like a LRU Cache. Here cap denotes the capacity of the cache and Q denotes the number of queries. Query can be of two types:
SET x y : sets the value of the key x with value y
GET x : gets the key of x if present else returns -1.
The LRUCache class has two methods get() and set() which are defined as follows.
get(key)   : returns the value of the key if it already exists in the cache otherwise returns -1.
set(key, value) : if the key is already present, update its value. If not present, add the key-value pair to the cache. If the cache reaches its capacity it should invalidate the least recently used item before inserting the new item.
In the constructor of the class the capacity of the cache should be intitialized.
more: https://practice.geeksforgeeks.org/problems/lru-cache/1
"""

class LRU:
    """
    Least Recently Used class
    """
    
    def __init__(self, c):
        self.c = c
        self.item = {}
        
    # LRU - Least recently used functionality is being used by reinserting any touch to a key value on the right hand side of dictionary. Any this that is on extreme left is least recently used item. 
    def set(self, k, v):
        if (k in self.item):
            self.item.pop(k)
            self.item[k] = v
        elif (len(self.item) == self.c):
            self.item.pop(list(self.item)[0])
            self.item[k] = v
        else:
            self.item[k] = v
        
    def get(self, k):
        if (k in self.item):
            val = self.item[k]
            self.item.pop(k)
            self.item[k] = val
            return val
        else:
            return -1

if __name__ == '__main__':
    cap = 2
    Q = 2
    
    lru_obj = LRU(cap)
    
    lru_obj.set(1,2)
    lru_obj.set(2,3)
    lru_obj.set(1,5)
    lru_obj.set(4,5)
    lru_obj.set(6,7)
    res = lru_obj.get(4)
    lru_obj.set(1,2)
    res = lru_obj.get(3)

    print(res)