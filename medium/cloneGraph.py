"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        return self.rec(node)

    
    def rec(self, node, mem = {}):
        if node.val in mem:
            return mem[node.val]
        
        new_node = Node(node.val, [])
        mem[node.val] = new_node

        for n in node.neighbors:
            neighbor = self.rec(n, mem)
            new_node.neighbors.append(neighbor)

        return new_node

        
