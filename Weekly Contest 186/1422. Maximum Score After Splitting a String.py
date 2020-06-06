class Solution:
    def maxScore(self, s: str) -> int:
        if not s:
            return 0
        curr_max = 0
        l, r = 0, s.count('1')
        for i in s[:-1]:
            if i == '0':
                l += 1
            else:
                r -= 1
            curr_max = max(curr_max, l+r)
            
        return curr_max
