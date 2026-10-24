class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minday=101
        maxday=101
        r=0

        while(r<len(prices)):
            if (prices[r]<minday):
                minday=maxday=prices[r]
            elif(prices[r]>maxday):
                maxday=prices[r]
            
            maxprofit=max(maxprofit,maxday-minday)
            r+=1

        return maxprofit
        