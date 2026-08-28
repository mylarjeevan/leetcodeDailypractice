class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        ls=[]
        ls.append(cost[0])
        ls.append(cost[1])
        for i in range(2,len(cost)):
            ls.append(min(ls[i-1],ls[i-2])+cost[i])
        return min(ls[-1],ls[-2])
        