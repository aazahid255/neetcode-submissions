# input: list of numbers candidates, an integer target
# output: list of list of integers, which reps all combinatinns that add up to target
# edge cases: candidates could be empty, target could be negative, or coul be 0

# backtracking, duplicates. 

# plan:
# res array
# if total == target: res.append(path[:]
# if index >= len(candiataes) or total > target return

# if we include the candidate, its fine bc it can be incldued agian in the future
# BUT if we are not includig the candiadte, skip all occurences of it so we dont have any duplicate combos

# return res at the end



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        candidates.sort()
        def dfs(i, path, total):
            if total == target:
                self.result.append(path[:])
                return
            if i >= len(candidates) or total > target:
                return
            
            path.append(candidates[i])
            dfs(i + 1, path, total + candidates[i])
            path.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, path, total)
        dfs(0, [], 0)
        return self.result