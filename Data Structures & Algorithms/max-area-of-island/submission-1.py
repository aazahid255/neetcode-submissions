class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        self.rows = len(grid)
        self.cols = len(grid[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= self.rows or col >= self.cols or grid[row][col] == 0:
                return
            self.cur_length += 1
            self.maxArea = max(self.maxArea, self.cur_length)
            grid[row][col] = 0

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                self.cur_length = 0
                dfs(row, col)
        return self.maxArea
        

        