"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


# input an adjacency list, with oen node as the iput
# output: the cloned graph (adjacency list)
# edge cases: empty node, only one node with no connections

# bfs? id also just assume a normal graph traversla

# we should just build the list from what we see, and then return that?

# start from the first node. 
# we do a dfs on this
# when we are at a node, we wanna add all its neighbors as a single list to our adj list
# once we are finished with that node, we increment? right bc like we start at 1 for example, then once that is done, we move onto the second node and its neighbors. 



class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)

            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node) if node else None
                
        
        
        