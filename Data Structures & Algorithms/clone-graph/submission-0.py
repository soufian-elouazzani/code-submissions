"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node :
            return None
        
        new_graphMap = {}

        clone = Node(node.val) 

        new_graphMap[node] = clone

        queue = collections.deque([node])

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in new_graphMap:
                    new_graphMap[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                new_graphMap[curr].neighbors.append(new_graphMap[neighbor])

        

        return new_graphMap[node]

