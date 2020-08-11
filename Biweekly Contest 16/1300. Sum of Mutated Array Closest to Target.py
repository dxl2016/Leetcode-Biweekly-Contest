class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        arr = sorted(arr, reverse=True)
        res = arr[0]
        while arr and target >= arr[-1]*len(arr):
            a = arr.pop()
            target -= a
        
        if not arr:
            return res
        return int(round((target-0.0001)/len(arr)))

