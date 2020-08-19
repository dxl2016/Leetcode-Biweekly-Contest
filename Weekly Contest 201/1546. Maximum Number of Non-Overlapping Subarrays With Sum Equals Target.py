class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        ans = 0
        cusum = 0
        tmp = {0:1}
        for each in nums:
            # print(tmp)
            cusum += each
            if cusum-target in tmp:
                ans += 1
                cusum = 0
                tmp = {0:1}
            else:
                if cusum not in tmp:
                    tmp[cusum] = 1
                else:
                    tmp[cusum] += 1
                    
        return ans

