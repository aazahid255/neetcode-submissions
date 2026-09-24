# input: integer array, represnting cost
# output: return min cost to climb the stairs
# edge cases: past the array indexing? cost array empty

# match; dp, climbing stairs problem

# recurrence relation: the minimum way to reach a certain step is the minimum way to reach out of the previous 2 steps
# we can store the minimum of the past 2 steps in the current step, and then keep moving forward.
# lets do bottom-up tabulation. we strat with checking base case of only 2 items in cost, where we store the min and return
# otherwise, we iterate until end of the array. the current step is equal to the minimum cost of the last 2 steps + the current cost of the step.
# return the last value in array

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        n = len(cost)
        
        dp = [0] * (n)

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[n - 2], dp[n-1])
        