# input: m x n grid with 3 possible values 
# output: grid modified in place
# edge cases: empty grid, only treasure, only land, only water

# match: dfs. similar to island problems we have already solved

# plan if not grid, return []
# we first define our dfs function
# the base case is obviously if the cell is a water cell, or out of bounds, we just return
# otherwise, there are things to do lol. 
# if we find a treasure chest, we also technically return, but we wanna return the "traversal value", basically how long it took to get there
# if we find land, we do a dfs on it. 

# then we loop through each cell. we have to do a dfs starting from each land cell.
# before u run the dfs, initialzie "traversal" to 0. once we reach a treasure chest in this call, we set the current cell to traversal
# if its water or treasure, our loop skips it


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return []

        rows = len(grid)
        cols = len(grid[0])
        inf = 2147483647

        q = deque()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
      
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))
        
        while q:
            cur_cell = q.popleft()
            orig_row = cur_cell[0]
            orig_col = cur_cell[1]
            for x, y in dirs:
                neighbor_row = orig_row + x
                neighbor_col = orig_col + y
                if  neighbor_row >= 0 and  neighbor_row < rows and neighbor_col >= 0 and neighbor_col < cols:
                    if grid[neighbor_row][neighbor_col] == inf:
                        grid[neighbor_row][neighbor_col] = 1 + grid[orig_row][orig_col]
                        q.append((neighbor_row, neighbor_col))
   

            
            
        