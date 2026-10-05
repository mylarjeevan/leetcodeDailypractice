class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If buying = True, we are allowed to buy
        # If buying = False, we are allowed to sell

        dp = {}  # key = (i, buying), value = max profit

        def dfs(i, buying):
            # Reached the end
            if i >= len(prices):
                return 0

            # Already calculated
            if (i, buying) in dp:
                return dp[(i, buying)]

            # Option 1: Do nothing
            cooldown = dfs(i + 1, buying)

            if buying:
                # Option 2: Buy
                buy = dfs(i + 1, not buying) - prices[i]

                dp[(i, buying)] = max(buy, cooldown)

            else:
                # Option 2: Sell
                sell = dfs(i + 2, not buying) + prices[i]

                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)