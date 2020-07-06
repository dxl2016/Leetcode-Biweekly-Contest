class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if not arr:
            return True
        arr = sorted(arr)
        f, s = arr[0], arr[1]
        d = s-f
        if len(arr) == 2:
            return True
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != d:
                return False
        return True

