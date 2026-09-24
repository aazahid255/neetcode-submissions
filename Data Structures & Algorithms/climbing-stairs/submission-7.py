# input: integer, represetnign steps of a staircase
# output: integer that reps distinct ways to reach top of staircase
# edge cases: n = 0, n = 1, n = 2

# match: dp, recurrence relation

# plan: lets define the relation: at 2, there are 2 ways to reach it. at 3, we can reach it in all the ways you reach the previous step (2) + 1, and all the ways you reach the 2 steps before (1) + 2. 

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n - 1]

        