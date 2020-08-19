class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for _ in range(n-1):
            tmp = ""
            for each in s:
                tmp += str(int(each) ^ 1)
            s = s+"1"+tmp[::-1]
            
        return s[k-1]

