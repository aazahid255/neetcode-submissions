# input: 2-d grid
# output: integer, either min number of minutes until whole board rotten, or -1 if it is impossible
# edge cases: empty grid, onyl one cell in grid, only rotten fruit so already rotten return 0

# bfs? add all the rotten fruit starting coords to a queue. this is the starting state
# also add all the fresh fruit coords to a set? or an array? 
# then, from the starting rotten coords, we do a bounds check firs tand then make all the beighboring fresh fruit rotten. if NO changes are made, we immediately return -1 bc no change in state and existence of fresh fruit still means we can never reach that state
# if we eventually reach only rotten, then we can return wahtebver our minute counter is

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        rotten_fruit = deque()
        fresh = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    rotten_fruit.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1
        if fresh == 0: return 0
        minutes = 0
        if not rotten_fruit: return -1
        while fresh > 0 and rotten_fruit:
            iterations = len(rotten_fruit)
            for _ in range(iterations):
                row, col = rotten_fruit.popleft()
                dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for x, y in dirs:
                    cur_row = row + x
                    cur_col = col + y
                    if cur_row >= 0 and cur_col >= 0 and cur_row < ROWS and cur_col < COLS:
                        if grid[cur_row][cur_col] == 1:
                            grid[cur_row][cur_col] = 2
                            fresh -= 1
                            rotten_fruit.append((cur_row, cur_col))
            minutes += 1
        if fresh == 0:
            return minutes
        else:
            return -1



        