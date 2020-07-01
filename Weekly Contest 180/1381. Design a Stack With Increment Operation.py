class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.ans = []

    def push(self, x: int) -> None:
        if len(self.ans) < self.size:
            self.ans.append(x)

    def pop(self) -> int:
        if self.ans:
            return self.ans.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.ans))
        for i in range(k):
            self.ans[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
