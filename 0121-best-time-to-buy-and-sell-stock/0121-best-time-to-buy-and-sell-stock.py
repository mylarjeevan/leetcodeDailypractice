class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mins=prices[0]
        cost=0
        profit=0
        for i in range(1,len(prices)):
            cost=prices[i]-mins
            profit=max(profit,cost)
            mins=min(mins,prices[i])
        return profit
            
        