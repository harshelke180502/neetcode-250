class StockSpanner:

    def __init__(self):
        self.stack=[]
        

    def next(self, price: int) -> int:
        days=1
        while self.stack and self.stack[-1][0]<=price:
            top=self.stack.pop()
            # print("Top",top)
            days+=top[1]
        self.stack.append([price,days])
        print(self.stack)
        return days          

                


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)