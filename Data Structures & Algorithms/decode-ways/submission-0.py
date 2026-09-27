# input: string with numbers, that maps to a coding of letters
# output: number of ways to decode the message
# edge cases: empty string?, leading 0 in the string? non-digits in the string?

# match: map?, dynamic programming? 

# all digits are a digit by themselves, other than 0. 1 or 2 followed by a 0 are also a digit. 1 or 2 can be followed by any digit 1-6 and be grouped tg. no other grouping exists. 
# brute force? -> iterating through every single substring, and seeing it it is in the range "1" -> "26" and checking if it is valid. 

# implement:
# iterate through the string, at each index

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            if(i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                res += dfs(i + 2)

            dp[i] = res

            return res

        return dfs(0) 
        
        