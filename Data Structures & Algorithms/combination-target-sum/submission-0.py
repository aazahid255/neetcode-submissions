# input: nums (array of distinct integers), target integer target
# output: list of lists, return all unique comvinatoins of nums where chosen numbers sum to target
# edge cses: no numbers sum to target, nums is empty, nums is only one number

# understand: backtracking, comvinatoin sum

# plan: option trees at each index:
# at the first index, we could keep including the first number. 
# include it until it is more than the target or equal to target, then return. if it was equal, no point in adding more nums! lets backtrack
# then we backtrack from teh first index. we then can add the next index, or the next number etc
# likely need a for loop bc we need all comvbinations
# no idea after that



class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.results = []
        def backtrack(path, remaining, index):
            if remaining == 0:
                self.results.append(path[:])
                return
            if remaining < 0:
                return
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(path, remaining - nums[i], i)
                path.pop()
        backtrack([], target, 0)
        return self.results
        