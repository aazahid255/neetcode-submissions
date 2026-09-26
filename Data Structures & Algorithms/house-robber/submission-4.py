# input: integer array nums
# output: max money i can rob without alerting police
# edge cases: one 1 house in nums, 2 houses in nums

# match: 1-d dp

# iterate through nums with a dp array
# declare dp array with all 0s
# at each index, i set the value to the sum of the current value, added to i-2
# i return the max of the value in either the last or second last index, bc that will cover all the jumps i can make


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        if n == 1 or n == 2:
            return max(nums)   
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
             
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return max(dp[n-1], dp[n-2])
        