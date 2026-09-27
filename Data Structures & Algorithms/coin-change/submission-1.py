# input: interger array of coins, and target integer amount
# output: fewest number of coins needs to make up target amount
# edge cases: if amount is 0, if amount is higher than all couins we have, if coins is empty

# match: 1-d dp, recursion 

# recurrence relation: if we take a large coin from an amount, the resutl is a smaller amount, and we just have to keep subtracting from that. 

# dp[i] is the minimum number of ways to reach a certain coin denomination
# dp[0] = 0
# if amount == 0, or we are above the amount, we are done and we return
# iterate through all coins in the array, if it is less than amount, run a dfs with the amount of coins we have, and on amount - coin. return the minimum of whatever we find


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            min_coins = 99999

            for coin in coins:
                if coin <= amount:
                    min_coins = min(min_coins, 1 + dfs(amount - coin))

            memo[amount] = min_coins
         
            return min_coins

        if dfs(amount) == 99999:
            return -1
        return dfs(amount)



        