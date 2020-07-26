class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(indices)
        tmp = [""]*n
        for i in range(n):
            tmp[indices[i]] = s[i]
        
        return "".join(tmp)

