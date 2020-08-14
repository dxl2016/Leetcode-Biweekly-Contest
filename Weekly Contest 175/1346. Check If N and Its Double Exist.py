class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        n = len(arr)
        for i in range(n):
            if arr[i]%2 == 0 and arr[i]//2 in arr and arr[i] != 0:
                return True
        counter = Counter(arr)
        if counter[0] > 1:
            return True
        
        return False

