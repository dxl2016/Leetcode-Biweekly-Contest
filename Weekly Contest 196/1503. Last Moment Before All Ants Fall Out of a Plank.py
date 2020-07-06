class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left = sorted(left, reverse=True)
        right = sorted(right)
        if left:
            l = left[0]-0
        if right:
            r = n-right[0]
        if left and right:
            return max(l,r)
        return l if left else r

