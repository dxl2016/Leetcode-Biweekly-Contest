class ProductOfNumbers:

    def __init__(self):
        self.res = [1]

    def add(self, num: int) -> None:
        if num != 0:
            self.res.append(num*self.res[-1])
        else:
            self.res = [1]

    def getProduct(self, k: int) -> int:
        if k >= len(self.res):
            return 0
        else:
            return self.res[-1]//self.res[-k-1]
        
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

