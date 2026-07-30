# input: array nums of unique integers
# output: list of list of integers, it is all possible permutaoitns
# edge cases: empty nums, only 1 num in nums

# match: backtracking

# plan: 
# at each index, im deciding the order. if i wanna add it or not. if i exclude, it eventually still HAS to be in my result. i cannot "pop" it
# my base case is if we reach len(nums). then, we aleays add and just recurse
# i start with including 1. once ive incldued a number, we dont ever add it back. go to the next index
# if i dont include it, i eventually have to include it later. what if i pop and add it to the "back" queue data structure?
# then, we return result after this is done
# path should be a queue
# recursive helper needs path and it needs index


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        def backtrack(path):
            if len(path) == len(nums):
                self.result.append(path[:])
                return
            
            for num in nums:
                # skip the current index
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()
                
        backtrack([])
        return self.result


        
        