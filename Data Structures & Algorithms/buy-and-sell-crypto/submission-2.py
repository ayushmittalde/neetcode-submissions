class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minp=prices[0]

        for i in range(1,len(prices)):
            profit=max(prices[i]-minp,profit)
            minp=min(minp,prices[i])
        
        return profit