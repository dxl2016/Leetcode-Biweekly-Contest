class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key = lambda x:x[1])
        # print(events)
        days = set()
        ans = 0
        for s, e in events:
            for t in range(s, e+1):
                if t not in days:
                    days.add(t)
                    ans += 1
                    break
        
        return ans

