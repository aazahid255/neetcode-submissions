class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        self.rows = len(grid)
        self.cols = len(grid[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= self.rows or col >= self.cols or grid[row][col] == 0:
                return 0
            grid[row][col] = 0

            return 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                self.cur_length = 0
                if grid[row][col] == 1:
                    self.maxArea = max(self.maxArea, dfs(row, col))
        return self.maxArea
        

        