class StockSpanner:

    def __init__(self):
        self.stock=[]
        self.i=-1

    def next(self, price: int) -> int:
        
        self.i+=1

        while len(self.stock) and (price>=self.stock[-1][0]) :
            self.stock.pop()
        
        if self.stock:
            ans= self.i - self.stock[-1][1]
        else :
            ans= self.i +1

        self.stock.append([price,self.i])
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)