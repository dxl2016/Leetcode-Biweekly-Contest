class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hA = sorted([0] + horizontalCuts + [h])
        vA = sorted([0] + verticalCuts + [w])
        max_h = -float('Inf')
        max_v = -float('Inf')
        for i in range(1, len(hA)):
            max_h = max(max_h, hA[i]-hA[i-1])
        for j in range(1, len(vA)):
            max_v = max(max_v, vA[j]-vA[j-1])
        return max_h*max_v % (10**9 + 7)
