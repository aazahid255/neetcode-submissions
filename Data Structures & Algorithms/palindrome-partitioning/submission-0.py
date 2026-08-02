# input: a string s
# output: a list of list of substrings, that are all palindromes
# edge cases: empty string, string with one word, an actual palindrome

# match: backtracking

# plan: 
# base cases: if it is a palindrome, we remove those characters from the string and keep exploring to see if the rest r palindromes
# if we ever get to a point where the string is empty, then we have found an occurnce of all strings being palindromes
# so what do we wanna do? - start with the first letter. if it is a substring, we recurse with the rest of the string and add our current substring to a result 
# if the letter is a palindrome, we immediatley add it, otherwise we keep going
# 




class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.cur_palindromes = []
        def dfs(i):
            if i >= len(s):
                self.result.append(self.cur_palindromes.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    self.cur_palindromes.append(s[i:j+1])
                    dfs(j + 1)
                    self.cur_palindromes.pop()

        dfs(0)
        return self.result

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
    
    

    

            
        