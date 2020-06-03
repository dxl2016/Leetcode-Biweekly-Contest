class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        n = len(startTime)
        ans = 0
        for i in range(0, n):
            if startTime[i] <= queryTime <= endTime[i]:
                ans += 1
        return ans
