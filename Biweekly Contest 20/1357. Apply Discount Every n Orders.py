class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.c = 0
        self.n = n
        self.discount = discount
        self.dic = {}
        for i,v in enumerate(products):
            self.dic[v] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.c += 1
        tot = 0
        for i in range(len(product)):
            tot += self.dic[product[i]] * amount[i]
        if self.c == self.n:
            tot *= (1-float(self.discount/100))
            self.c = 0
        return tot
            

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

