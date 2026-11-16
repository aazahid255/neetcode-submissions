# input: nums, array of numbers
# output: min number of jumps
# edge cases> empty nums -> jump would be 0, only 1 num in array, so jumps would be 0, 2 numbers. reaching a 0

# match: jump game, greedy algorithm

# plan:
# at each array, we always wanna take the furthest jump. get the current jump, and see if its longer than the current jump, or taking a jump to that index and then taking that jump would be more beneficial. basically testing the max jump at each index. so jump to the max number in each jump window, until we reach the end.
# return # of jumps with this greedy algorithm

class Solution:
    def jump(self, nums: List[int]) -> int:
        num_jumps = 0
        l = 0  # Left boundary of our current jump window
        r = 0  # Right boundary of our current jump window
        
        while r < len(nums) - 1:
            farthest = 0
            
            # 1. Scan only the stones inside your current window [l, r]
            # to find the absolute furthest reach.
            temp = r + 1
            while l <= r:
                farthest = max(nums[l] + l, farthest)
                l += 1
            l = temp
            r = farthest
            num_jumps += 1
            # 2. Once the window is scanned, take the jump!
            # Update l to be just outside your old window (r + 1)
            # Update r to be your new farthest reach.
            
            # 3. Add 1 to num_jumps
            
        return num_jumps
        