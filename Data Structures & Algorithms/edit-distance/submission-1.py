class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def dfs(i, j):
            if (i,j) in dp:
                return dp[(i, j)]
            if i == len(word1):
                dp[(i, j)] = len(word2) - j
                return dp[(i, j)]
            if j == len(word2):
                dp[(i, j)] =  len(word1) - i
                return dp[(i, j)]

            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i+1, j+1)
                return dp[(i, j)]
            else:
                dp[(i, j)] = 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
                return dp[(i, j)]
        return dfs(0, 0)
        