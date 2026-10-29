# input: integer array nums
# output: integer, maximum output of the array
# edge cases: neg numbers, empty array, only one nyumber in array

# start with subarray at the beginning
# u add the num.
# if current num is larger than the array we already have, we start a new subarray and keep adding it. if it isnt, keep building this array
# return the max of the dp array


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i] + dp[i - 1]:
                dp[i] = nums[i]
                continue
            dp[i] = nums[i] + dp[i - 1]
        return max(dp)

        