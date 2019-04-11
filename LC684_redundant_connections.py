class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.rank = 0

class DisjointSet:
    def __init__(self):
        self.map = {}
        
    def make_set(self, data):
        if data not in self.map:
            node = Node(data)
            node.parent = node
            self.map[data] = node
        return self.map[data]
        
    def find_set(self, node):
        parent = node.parent
        if parent == node:
            return parent
        node.parent = self.find_set(parent)
        return node.parent
    
    def union(self, data1, data2):
        node1 = self.make_set(data1)
        node2 = self.make_set(data2)
        
        parent1 = self.find_set(node1)
        parent2 = self.find_set(node2)
        
        if parent1.data == parent2.data:
            return False
        
        if parent1.rank >= parent2.rank:
            parent1.rank = (parent1.rank + 1 if parent1.rank == parent2.rank else parent1.rank)
            parent2.parent = parent1
        else:
            parent1.parent = parent2
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds = DisjointSet()
        redundant = [-1, -1]
        for v1, v2 in edges:
            if not ds.union(v1, v2):
                redundant = [v1, v2]
                
        return redundant

