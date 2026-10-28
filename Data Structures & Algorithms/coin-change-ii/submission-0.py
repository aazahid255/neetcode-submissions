# input: integer amount, integer array coins
# output: integer, amount of ways we can make the combinatoins
# edge cases: couns emty, amount negative or 0, coins only one number

# match: 2-d dp, coin change I

#brute force: trying every single comvinatoin 
# recurrence relation: each index can be reached by the sum of all the coins minus that current amount
# at each index, we a-c is a valid value in dp, we add it to the current index for dp. at the end, we return dp[amonunt] bc that will be all the ways to get to amount


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i-c]
        return dp[amount]