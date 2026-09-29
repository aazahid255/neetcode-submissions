# input, integer array nums
# output: integer
# edge cases: nums empty, negative numbers, 0, equal numbers

# match: 1-d dp? 

# at aech index, we loop through all the numberes before, if there are no numbers less than our current numbner, we set dp[i] = 1
# if there is any numbers less than it, we get the mex length. max(1 + dp[i - j])
# return max(dp)



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            max_length = -1
            for j in range(i):
                if nums[j] < nums[i]:
                    max_length = max(max_length, 1 + dp[j])
            dp[i] = max(1, max_length)
        return max(dp)
                    
        # dp = [1, 1, ]