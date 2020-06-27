class Solution:
    def average(self, salary: List[int]) -> float:
        if not salary:
            return 0
        max_s, min_s = max(salary), min(salary)
        return (sum(salary)-max_s-min_s)/(len(salary)-2)

