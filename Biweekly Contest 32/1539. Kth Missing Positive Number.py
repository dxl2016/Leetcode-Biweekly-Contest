class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        tmp = 1
        res = 0
        while(True):
            if tmp in arr:
                tmp += 1
            else:
                res += 1
                if res == k:
                    return tmp
                tmp += 1

