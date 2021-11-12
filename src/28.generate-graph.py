"""
author: Dr. Mohammed Zia
https://www.linkedin.com/in/zia33

Problem Statement:
Generate graph
more: 
"""
        
class Graph:
    def __init__(self, edges, n):
        self.adj_list = [[] for i in range(n)]
        
        for (src, dest) in edges:
            self.adj_list[src].append(dest)
            self.adj_list[dest].append(src)
        
if __name__ == '__main__':

    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
    ]
    
    n = 15
    
    graph = Graph(edges, n)