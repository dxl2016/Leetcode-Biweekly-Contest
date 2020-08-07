class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = sorted(arr)
        tmp = {}
        for i in arr:
            res = bin(i)[2:].count("1")
            if res not in tmp:
                tmp[res] = [i]
            else:
                tmp[res] += [i]
        tmp = sorted(tmp.items())
        ans = []
        for each in tmp:
            ans += each[1]
        
        return ans

