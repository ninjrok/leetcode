class Vertex:
    def __init__(self, _id):
        self.id = _id
        self.neighbors = []
        
    def get_neighbors(self):
        return self.neighbors
    
    def add_neighbor(self, nbr):
        self.neighbors.append(nbr)
       
    
class Graph:
    def __init__(self):
        self.vertices = {}
        
    def get_vertex(self, _id):
        return (self.vertices[_id] if _id in self.vertices else None)
        
    def add_vertex(self, _id):
        if _id not in self.vertices:
            self.vertices[_id] = Vertex(_id=_id)
            
    def add_edge(self, a, b):
        self.add_vertex(a)
        self.add_vertex(b)
        self.vertices[a].add_neighbor(self.vertices[b])


class Solution:
    def dfs(self, vertex, visited):
        if not vertex or vertex in visited:
            return
        
        visited.append(vertex)        
        for nbr in vertex.get_neighbors():
            self.dfs(nbr, visited)
        
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n_rooms = len(rooms)
        if n_rooms == 1:
            return True
        
        graph = Graph()
        for i in range(n_rooms):
            for j in range(len(rooms[i])):
                graph.add_edge(i, rooms[i][j])
        
        visited = []
        self.dfs(graph.get_vertex(0), visited)
        
        return (True if len(visited) == n_rooms else False)

