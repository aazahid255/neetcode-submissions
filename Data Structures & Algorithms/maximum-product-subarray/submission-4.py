# input: integer array nums 
# output: subarray with largest product
# edge cases: nums is empty, negative numbers, only one number

# match: 1-d dp, recursion

# at each index, we take either the max of the current num, or the product of this num and the previous number

# every array is a product with itself

# iterate eyhtough each one, if the product of this number and the previous one is larhger than current num, update it. othereise, leave it, and mvoe on. at the end, we return the amx of the array

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = [0] * n
        min_dp = [0] * n

        min_dp[0] = nums[0]
        max_dp[0] = nums[0]

        for i in range(1, n):
            candidates = (nums[i], max_dp[i-1] * nums[i], min_dp[i-1] * nums[i])
            max_dp[i] = max(candidates)
            min_dp[i] = min(candidates)
        return max(max_dp)
        