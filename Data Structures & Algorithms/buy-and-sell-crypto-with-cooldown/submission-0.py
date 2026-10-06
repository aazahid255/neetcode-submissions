# input: int array price
# output: integer, max profit
# edge cxases: pruices is only 1 number, 0 is tge stock

# sliding window?, we wither buy at a certain time and then have to sell it later
# at any point, we are either looking to buy or sell, we need a decision tree where we weither buy/sell every stock

# recurrence relation would be buyig or selling at current price. 2-d matrix of buy/sell and its each stock? and the current cell is the profit we get from buying or selling it?
# so we need 3 states, resting, holding, and sold

# the recurrsne realtion for 
# sold[i] = hold[i-1] + prices[i]
# hold[i] = max(hold[i-1], rest[i-1] - price)
# rest[i] = max(rest[i-1], sold[i-1])


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        sold = [0] * n
        hold = [0] * n
        rest = [0] * n
        sold[0] = 0
        rest[0] = 0
        hold[0] = -prices[0]
        for i in range(1, n):
            sold[i] = hold[i-1] + prices[i]
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])
            rest[i] = max(rest[i-1], sold[i-1])
        return max(sold[-1], rest[-1])


