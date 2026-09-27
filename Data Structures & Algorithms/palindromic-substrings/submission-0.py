# input: string s
# output: integer, that represents the number of substeings s that are palindroems
# edge cases: empty string, 1 letter in string, string with multiple palindromes, "AAAA"

# match: dp, palindrome questoin, center pattern

# implement:
# iterate for both odd and even subsrrings. start from the first index, and while l == r and theyre not out of bounds, we add 1 to our palindrome counter. we return this palindrome counter at the end of both iteratoins, even if there are duplicates

class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0

        for i in range(len(s)):
            l, r = i, i
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                palindromes += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                palindromes += 1
                l -= 1
                r += 1
            
        return palindromes
            
            

        