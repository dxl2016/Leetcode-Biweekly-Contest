class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        res = [0 for _ in range(len(light))]
        curr_far = 0
        cum = 0
        ans = 0
        for i in light:
            res[i-1] = 1
            curr_far = max(curr_far, i-1)
            if cum == i-1:
                while(True):
                    if cum<len(light) and res[cum] == 1:
                        cum += 1
                    else:
                        break
                if cum-1 == curr_far:
                    ans += 1
        return ans

