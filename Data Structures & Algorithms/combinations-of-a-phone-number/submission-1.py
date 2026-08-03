# input: string of digits
# output: a list, which has all possible letter combinations from those digits
# edge cases: empty digits, only one digit

# match: kinda subsetsy problem, backtracking for sure 

# plan: for loop pattern will definitley be needed
# at each index, we either include the current letter, or we move on and include the next one
# we have to do that for every integer in the string
# 100% need a map so that we can get the letters that occur to each integer
# we have a path vairable. when index is equal to len(digits), we add this path to our results array
# at each index of our digits string, we want to loop through the map. we either include the digit, or we dont and move on to the next one. once we include a digit, we move onto the next index and backtrack with that
# once we are out of the backtracking call, we backtrack without this character included

# return results at the end



class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        self.result = []
        self.digit_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def backtrack(index, path):
            if index == len(digits):
                self.result.append(path)
                return
            for char in self.digit_map[digits[index]]:
                backtrack(index + 1, path + char)
                # do we need another backtracking call?
        backtrack(0, "")
        return self.result

        