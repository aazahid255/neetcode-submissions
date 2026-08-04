# input: 2d grid
# output: number of islands (integer)
# edge cases: empty grid, all 0s

# match: dfs

# plan: 
# explore all 1s in an island, once we visit a node we mark it as visited. 
# intialzie a count
# dont need a set bc we can just set 1s to 0s
# itearte through grid
# if we see a 1, recursively visit every 1 that is reachable. mark visited 1s as 0s.
# increment when we see a 1 bc that is our number of groups
# return number of groups


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        self.len_row = len(grid)
        self.len_col = len(grid[0])
            
        island_count = 0
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= self.len_row or c >= self.len_col or grid[r][c] == '0':
                return

            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # MAIN LOOP
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r + 1, c)
                    dfs(r - 1, c)
                    dfs(r, c + 1)
                    dfs(r, c - 1)
                # If we find a piece of land ('1'):
                # 1. Increment island_count
                # 2. Call dfs(r, c) to sink this entire connected island
                
        return island_count
        