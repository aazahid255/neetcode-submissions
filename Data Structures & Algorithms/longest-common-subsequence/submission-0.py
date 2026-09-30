# input: 2 strings
# output: integer, representing length of longest common subsequence
# edge cases: empty strings, is text1 always les than text2?, non alphanumeric chars

# match: dynamic programming
# recurrnese realtion, - the smaller word always has to be a subseuqenve of the other, a larger word cannot be a subsequenve of a smaller. u either can include a character in the recursion or not, and then compare if those r the same.




class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1) + 1
        n2 = len(text2) + 1
        dp = [[0 for _ in range(n2)] for _ in range(n1)]
        for row in range(1, n1):
            for col in range(1, n2):
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col-1])
        return dp[n1 - 1][n2 -1]