# bottom-up solution

# rec relation: dp[i, s] = dp[i+1, s] or dp[i+1, s + nums[i]]



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = set([0])
        for n in nums:
            new_dp = set()
            for d in dp:
                print(d)
                new_dp.add(d)
                new_dp.add(d + n)
            dp = new_dp
            if target in dp:
                return True
        return False
        