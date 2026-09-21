# input: n, list of edges
# output: an integer, which is the number of connected components
# edge cases: only 1 node, all disconnected components

# match: dfs or bfs works, will prolly do graph dfs, need a set as well

# plan: 
# visited set
# create adj list
# run dfs with cur_ndoe and prev_node
# if node is in the visited set, we just return, no need to return false
# add node to visited set
# run dfs on all the nodes its connected to 
# we do not remove from visited set
# return at the end of the funciton call
# after a dfs call is made, we increment our connected components
# our visited set will contain however many are visited, once this set is equal to n aftre a dfs call, we can return that integer

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.visitSet = set()
        self.adjList = {i:[] for i in range(n)}
        con_components = 0
        for node, ver in edges:
            self.adjList[node].append(ver)
            self.adjList[ver].append(node)

        def dfs(node, prev):
            if node in self.visitSet:
                return
            
            self.visitSet.add(node)
            for vertex in self.adjList[node]:
                if vertex == prev:
                    continue
                dfs(vertex, node)
            
            return
        
        for i in range(n):
            if i not in self.visitSet:
                dfs(i, -1)
                con_components += 1
            if len(self.visitSet) == n:
                return con_components

        