class Vertex:
    def __init__(self, _id):
        self.id = _id
        self.trustees = []
        self.trusts = []
        
    def create_trust(self, vertex):
        self.trusts.append(vertex)
        
    def is_trusted_by(self, vertex):
        self.trustees.append(vertex)
        
    def n_trusts(self):
        return len(self.trusts)
        
    def n_trustees(self):
        return len(self.trustees)
            

class Graph:
    def __init__(self):
        self.vertices = {}
        
    def count(self):
        return len(self.vertices)
        
    def add_vertex(self, _id):
        self.vertices[_id] = Vertex(_id=_id)
        
    def create_trust(self, a, b):
        if a not in self.vertices:
            self.add_vertex(a)
        if b not in self.vertices:
            self.add_vertex(b)
        
        self.vertices[a].create_trust(self.vertices[b])
        self.vertices[b].is_trusted_by(self.vertices[a])
        
    def __iter__(self):
        for vertex in self.vertices.values():
            yield vertex


class Solution:    
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        g = Graph()
        
        for a, b in trust:
            g.create_trust(a, b)
            
        if g.count() != N:
            if N == 1:
                return 1
            else:
                return -1
        
        for vertex in g:
            if vertex.n_trustees() == N-1 and vertex.n_trusts() == 0:
                judge = vertex.id
                break
        else:
            judge = -1
            
        return judge

