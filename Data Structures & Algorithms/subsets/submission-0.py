
# input: nums of unique integers
# output: return all possible usbests of nums (list of lists of integers)
# edge cases: empty list, only one number in list

# match: backtrackiung (subset shape)

# plan: 
# solution: if the list contains only numbers from the input
# promising: if it contains a number from nums, if it dfoesnt we can breaj
# start from [], and build from there

# brute force: add an empty list, then at each iteration, we add the number itself and 1 of 
# each extra number in the list, then we add 2 of each number, and thus on, seems incredibly inefficnent
# probbaly like O(n!) time 

# backtracking, base case is if our index has hti len nums, then add it to resutls array
# otherweise, we either include or excluse the current index of nums and keep exploring






class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        path = []
        index = 0
        def backtrack(path, index):
            if index == len(nums):
                self.results.append(path[:])
                return
            path.append(nums[index])
            backtrack(path, index + 1)
            path.pop()
            backtrack(path, index + 1)
        backtrack(path, index)
        return self.results
        