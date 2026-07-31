# input: an integer n
# output: a list of strings, which are all well-formed parntheses
# edge cases: n = 0? impossible, edge cases with the parentheses and how they couldbe formed
# "()(), (()), (()())"

# match: backtracking, kind of subsetty?

# plan:
# base cases:
# if length of string is equal to n * 2
# check if its a valid parentheses or not. if it is, add it to our list. if its not, backtrack
# at each index, we either add a ( or a ). then we recurse with this. 
# this way, we can explore a ( or a ) at every index and eventually check if its a valid parentheses

# helper functoin to check if its valid may behelpful


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        def backtrack(cur_string, open_count, close_count):
            if open_count > n:
                return
            if close_count > open_count:
                return
            if len(cur_string) == (n * 2): # base case
                self.result.append(cur_string)
                return
            if open_count < n: backtrack(cur_string + "(", open_count + 1, close_count)
            if close_count < open_count: backtrack(cur_string + ")", open_count, close_count + 1)
        backtrack("", 0, 0)
        return self.result




        