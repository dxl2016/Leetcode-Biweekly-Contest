class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        
        s = max(arr)
        n = len(arr)
        l, r = 0, 1
        prev = 0
        res = 0
        while(arr[0] != s):
            now = max(arr[l], arr[r])
            if prev == now:
                res += 1
            else:
                prev = now
                res = 1
            if res == k:
                return prev
                
            if arr[l] > arr[r]:
                a = arr[r]
                arr.remove(a)
                arr += [a]
            else:
                a = arr[l]
                arr.remove(a)
                arr += [a]
        
        return arr[0]

