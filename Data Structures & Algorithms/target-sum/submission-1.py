


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # {i, cur_sum} -> number of ways
        def backtrack(i, cur_sum):
            if (i, cur_sum) in dp:
                return dp[(i, cur_sum)]
            if i == len(nums):
                if cur_sum == target:
                    return 1
                else:
                    return 0
            dp[i, cur_sum] = (backtrack(i + 1, cur_sum + nums[i]) +
            backtrack(i + 1, cur_sum - nums[i]) )
            return dp[i, cur_sum]
        return backtrack(0, 0)
        
        