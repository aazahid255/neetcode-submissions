# input: integer array nums
# outpot boolean true or false
# edgw cases: nums empty, nums only one number

# matfch: 1-d dp, binary serach?
# recurrence relation: a single number can be compared to the rest of the array
# 

# base case: if sum > target, or i > index of array
# we make 2 recurisve calls, either adding current num, or moving forward withoout adding current num
# return an or for these calls, bc either can return true

# what is recurrence realtion? 

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        target = total // 2
        memo = {}
      
        def dfs(curSum, i):
            if ((curSum, i) in memo):
                return memo[(curSum, i)]
            if curSum == target:
                return True
            if curSum > target or i >= len(nums):
                return False

            memo[(curSum, i)] = dfs(curSum, i + 1) or dfs(curSum + nums[i], i + 1)
            return dfs(curSum, i + 1) or dfs(curSum + nums[i], i + 1)
        return dfs(0, 0)