# input: 2d grid matrix
# output: an integer, which represnets the minimum number of minutes that must elapse unitl zero fresh fruits rmain, -1 if not possible
# edge case: empty grid, n x n grid?

# match: bfs, do queue like search from all the rotten fruits until we cant anymore


# plan: iterate through grid and find where all the rotten fruit are 
# every iteration, we go throuhg all the rotten fruit. we check all cells verical and adjcaent to them. if there is a fresh fruit in any of those cells, we change it to a rotten fruit and push it to the back of the queue to process later. 
# we should also keep a count of all the fresh fruit. if we reach a point where the number of fresh fruit has not changed in an interation and there are still fresh fruit in the grid, then we will never be able to reach zero, so we retuen -1
# if the length of our fresh fruit counter reaches 0, we return our iteration number




class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        if not rotten:
            return -1
        iterations = -1
        while rotten:
            len_queue = len(rotten)
            for i in range(len_queue):
                cur_cell = rotten.popleft()
                orig_row = cur_cell[0]
                orig_col = cur_cell[1]
                for x, y in dirs:
                    cur_row = orig_row + x
                    cur_col = orig_col + y
                    if cur_row >= 0 and  cur_row < rows and cur_col >= 0 and cur_col < cols:
                        if grid[cur_row][cur_col] == 1:
                            grid[cur_row][cur_col] = 2
                            fresh -= 1
                            rotten.append((cur_row, cur_col))
            iterations += 1
        if fresh == 0:
            return iterations
        else:
            return -1
            
            
            
        
