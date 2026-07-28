# input: list of nums, which might have duplicates
# putput: all possilble subsets
# edge cases: empty array

# match: backtracking, include/exclude pattern

# plan: cant we just use the same plan?


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.subsets = []
        nums.sort()
        def backtrack(path, index):
            if index == len(nums):
                self.subsets.append(path[:])
                return
            path.append(nums[index])
            backtrack(path, index + 1)
            if path: dupe_num = path.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtrack(path, index + 1)
        backtrack([], 0)
        return self.subsets