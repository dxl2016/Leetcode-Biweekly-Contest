class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        t = []
        c = 0
        for i in range(0, n):
            for j in range(i, n):
                c = sum(nums[i:j+1])
                t.append(c)
        t = sorted(t)
        return sum(t[left-1:right])

