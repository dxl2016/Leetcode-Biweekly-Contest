class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        res = -float("Inf")
        for i in range(len(arr)-1, -1, -1):
            res = max(res, arr[i])
            ans.append(res)
        
        return (ans[::-1][1:]+[-1])

