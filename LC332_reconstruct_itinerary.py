class Vertex:
    def __init__(self, _id):
        self.id = _id
        self.neighbors = []
        
    def add_neighbor(self, nbr):
        self.neighbors.append(nbr)
        
    def neighbor_id(self, nbr):
        return nbr.id
        
    def get_neighbors(self):
        return iter(sorted(self.neighbors, key=self.neighbor_id))


class Graph:
    def __init__(self):
        self.vertices = {}
        self.unvisited_edges = []
        
    def root(self):
        return self.vertices['JFK']
        
    def add_vertex(self, a):
        if a not in self.vertices:
            self.vertices[a] = Vertex(_id=a)
        
    def add_edge(self, a, b):
        self.add_vertex(a)
        self.add_vertex(b)
        self.unvisited_edges.append((a, b))
        self.vertices[a].add_neighbor(self.vertices[b])
        
    def not_visited(self, edge):
        if edge in self.unvisited_edges:
            self.unvisited_edges.remove(edge)
            return True
        else:
            return False


class Solution:
    def dfs(self, graph, vertex, itinerary):
        for nbr in vertex.get_neighbors():
            if graph.not_visited((vertex.id, nbr.id)):
                self.dfs(graph, nbr, itinerary)
        itinerary.insert(0, vertex.id)
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if len(tickets) == 0:
            return ['JFK']
        
        graph = Graph()
        
        for source, destination in tickets:
            graph.add_edge(source, destination)
        
        itinerary = []
        self.dfs(graph, graph.root(), itinerary)
        
        return itinerary

