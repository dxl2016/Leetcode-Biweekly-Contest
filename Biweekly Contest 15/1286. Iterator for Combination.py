class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.cum = 0
        self.n = len(characters)
        self.characters = characters
        self.combinationLength = combinationLength
        self.end = math.comb(self.n, self.combinationLength)
        self.a = list(combinations([i for i in range(self.n)], self.combinationLength))
        
    def next(self) -> str:
        if self.cum < self.end:
            idx = self.a[self.cum]
            self.cum += 1
            ans = ""
            for i in idx:
                ans += self.characters[i]
            return ans
        
    def hasNext(self) -> bool:
        if self.cum == self.end:
            return False
        return True

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

