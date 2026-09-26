# input: integer array nums
# output: max money you can rub 
# edge cases: 1st and 2nd are base cases

# match: house robber 1, 1-d dp

# same pattern to identify most money by robbing
# however we need some type of wrap around pattern for the first and last
# i think we can do normal solutoin, but just subtract the value of the first integer array from the final box, and get the max then 

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or n == 2:
            return max(nums)

        first_only = nums[0:n-1]
        last_only = nums[1:n]

        rob1, rob2 = 0, 0
        for n in first_only:
            cur_max = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = cur_max

                
        rob1, rob2 = 0, 0
        for n in last_only:
            cur_max_2 = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = cur_max_2


        return max(cur_max, cur_max_2)
        