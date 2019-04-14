class Vertex:
    def __init__(self, key):
        self.id = key
        self.neighbors = {}
        
    def add_neighbor(self, nbr):
        self.neighbors[nbr.id] = nbr
    
    def get_neighbors(self):
        return self.neighbors.values()
    
class Graph:
    def __init__(self, n):
        self.vertices = {}
        self.count = n
        
    def add_vertex(self, key):
        self.vertices[key] = Vertex(key=key)
    
    def add_edge(self, v1, v2):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        
        self.vertices[v1].add_neighbor(self.vertices[v2])
        return self.vertices[v1], self.vertices[v2]
        
    def __iter__(self):
        return iter(self.vertices.values())

class Solution:
    def move_vertex(self, vertex, b1, b2):
        v = b1.pop(vertex.id)
        b2[v.id] = v
        return b1, b2
    
    def dfs(self, vertex, white, gray, black):
        white, gray = self.move_vertex(vertex, white, gray)
        for nbr in vertex.get_neighbors():
            if nbr.id in black:
                continue
            elif nbr.id in gray:
                return True
            elif self.dfs(nbr, white, gray, black):
                return True
        gray, black = self.move_vertex(vertex, gray, black)
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        g = Graph(numCourses)
        
        white = {}
        gray = {}
        black = {}
        
        for req1, req2 in prerequisites:
            v1, v2 = g.add_edge(req1, req2)
            if v1 not in white:
                white[v1.id] = v1
            if v2 not in white:
                white[v2.id] = v2
        
        while len(white) > 0:
            vertex = next(iter(white.values()))
            if self.dfs(vertex, white, gray, black):
                return False
        return True

