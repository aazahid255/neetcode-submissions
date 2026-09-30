# input: 2 integeres, that represent the dimensions of grid
# output: unique paths (integer) to get to bottom right corner
# edge cases: m is 1, n is 0, 1x0, 

# match: 2-d dp, set?
# recurrence realtion of a signel tile = suming up all its neighbors ways to get there
# so we start at the top left tile, and set dp[0][0] = 1. theres one way to visit this tile. then we iterate through the array. 
# at each tile, with bounds checking, we add up the number from the dp array in the tile above and to the left of it, bc we can only move down or irght. thats the number of ways to reach that tile.
# we return wahts in the bottom left for the dp array

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for row in range(m):
            for col in range(n):
                print(dp[row][col])
                if (row - 1 >= 0):
                    dp[row][col] += dp[row - 1][col]
                if (col - 1 >= 0): 
                    dp[row][col] += dp[row][col - 1]
        return dp[m - 1][n - 1]
        