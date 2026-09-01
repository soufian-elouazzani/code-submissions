"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}

        clone = Node(node.val)
        visited[node] = clone

        queue = collections.deque()
        queue.append(node)
        while queue :
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
        
                visited[curr].neighbors.append(visited[neighbor])  
                
        
        return visited[node]

