import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [] #tails greedily builds the LIS

        for num in nums:
            if len(tails) == 0:
                tails.append(num)
                continue
            
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        
        return len(tails)