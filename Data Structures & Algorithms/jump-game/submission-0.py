class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest_reachable = 0
        for i in range(len(nums)):
            if i > farthest_reachable:
                return False
            farthest_reachable = max(farthest_reachable, i + nums[i])
        return True
        