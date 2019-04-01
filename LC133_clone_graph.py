"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:    
    def dfs(self, node, visited):
        if node.val in visited:
            return visited[node.val]
        
        visited[node.val] = Node(val=node.val, neighbors=[])
        # print('Node: {}, Nbrs: {}'.format(node.val, node.neighbors))
        
        for nbr in node.neighbors:
            node_nbr = self.dfs(nbr, visited)
            if node_nbr:
                visited[node.val].neighbors.append(node_nbr)
            
        return visited[node.val]
        
            
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        return self.dfs(node, {})

