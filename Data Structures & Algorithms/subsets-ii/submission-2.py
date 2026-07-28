# input: list of nums, which might have duplicates
# putput: all possilble subsets
# edge cases: empty array

# match: backtracking, include/exclude pattern

# plan: cant we just use the same plan?


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.subsets = []
        self.copies = []
        def backtrack(path, index):
            if index == len(nums):
                subset = sorted(path)
                if subset not in self.copies:
                    self.copies.append(subset[:])
                    self.subsets.append(path[:])
                return
    
            path.append(nums[index])
            backtrack(path, index + 1)
            path.pop()
            backtrack(path, index + 1)
        backtrack([], 0)
        return self.subsets