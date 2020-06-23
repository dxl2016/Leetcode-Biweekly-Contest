class Solution:
    def findLucky(self, arr: List[int]) -> int:
        if not arr:
            return -1
        temp = {}
        for i in arr:
            try:
                temp[i] += 1
            except:
                temp[i] = 1
        ans = {k:v for (k,v) in temp.items() if k == v}
        if ans:
            return max(ans.values())
        else:
            return -1

