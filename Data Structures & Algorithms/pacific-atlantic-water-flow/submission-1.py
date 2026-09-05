# input: grid with heights
# output: a list of the coordinates where where can flow from that cell to the pacific and atlantic oceans
# edge cases: empty grid, 1 cell in grid

# match: dfs, becasue at aech cell, we wanna keep going until we can either reach pacific or atlantic, or we cant anymore. if in our dfs calls we reach both pacific or atlatnic ocean, we just add it to our list of coordinates

# plan:
# loop over all the cells in the grid with a dfs
# in this dfs, we should have 2 "flags", pacific and atlantic. if at any point, we hit cols < 0 or rows < 0, we have hit pacific. if our rows > rows and col > cols, we have hit atlantic. once those r both true, we can add it to our list of coords
# then we check all 4 directions. if the cell at the direction is equal or less, we do a dfs on it too (so that we can keep searching). we have 2 base cases, either we can no longer serach or we have hit both pacfiic and aatlantic
# lets say at a cell, we can not run any of the 4 directions. we should return then as a base case. 





class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.coords = []
        rows = len(heights)
        cols = len(heights[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row, col):
            if row < 0 or col < 0:
                self.pacific = True
                return
            if row >= rows or col >= cols:
                self.atlantic = True
                return
            
            self.visited.add((row, col))
            for x, y in dirs:
                new_row = row + x
                new_col = col + y
                if new_row < 0 or new_col < 0:
                    self.pacific = True
                elif new_row >= rows or new_col >= cols:
                    self.atlantic = True
                elif heights[new_row][new_col] <= heights[row][col]:
                    if (new_row, new_col) not in self.visited:
                        dfs(new_row, new_col)
            return
                

        for row in range(rows):
            for col in range(cols):
                self.pacific = False
                self.atlantic = False
                self.visited = set()
                dfs(row, col)
                if self.pacific and self.atlantic:
                    self.coords.append((row, col))
        return self.coords
        