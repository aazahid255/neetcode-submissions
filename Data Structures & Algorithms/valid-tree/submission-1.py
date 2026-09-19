# input: list of undirected edges, given n nodes that are labeled from n to n-1
# output: boolean, if the graph is valid or not
# edge cases: cycle, n = 0, n = 1, no edges at all

# match: graph dfs?
# when it is not valid: first when there is a cycle, so have a set for cycle detection
# all components must be connected
# lets do dfs on everything, returning false if we ever have a cycle
# we have a completed set for each dfs. at the end of the dfs call, we can set max_set_size to the size this set is. at the end, if max set size is not n, it never included all nodes, and we did not have a valid tree
# create an adjacency list


# implement:
# create adj list
# decalre cycleSet
# declare completeSet
# do a dfs with the current node
# if the node is in the cycle set, return false
# if there is no nodes in the adj list mpa, return true
# add the current node to our cycle set
# do a dfs on all the nodes its connected to
# then, remove this node from the cycle set
# add it to the complete set
# after a dfs is done, update the size of the complete set
# once all dfs is done, if size of complete set is not equal to n, return false, else return true


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.adjList = {i:[] for i in range(n)}
        for node, con in edges:
            self.adjList[node].append(con)
            self.adjList[con].append(node)
        print(self.adjList)
        self.cycleSet = set()

        def dfs(node, prev_node):
            if node in self.cycleSet:
                return False

            
            self.cycleSet.add(node)
            for vertex in self.adjList[node]:
                if vertex != prev_node:
                    if not dfs(vertex, node): return False
            return True
            
        if not dfs(0, -1): return False
        return len(self.cycleSet) == n






        