class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        length=len(prices)

        if (length)==1:
            return 0

        for i in range (1,length):
            if prices[i-1]<prices[i]:
                profit+=prices[i]-prices[i-1]
        
        return profit
        