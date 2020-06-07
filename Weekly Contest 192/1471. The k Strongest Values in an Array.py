class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        if not arr:
            return
        arr = sorted(arr, reverse=False)
        n = len(arr)
        mid_idx = (n-1)//2
        mid = arr[mid_idx]
        l, r = 0, n-1
        ans = []
        while(len(ans)<k):
            if abs(arr[r]-mid) >= abs(arr[l]-mid):
                ans.append(arr[r])
                r -= 1
            else:
                ans.append(arr[l])
                l += 1
        return ans
