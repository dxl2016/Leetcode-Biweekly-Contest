class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        counter = collections.Counter(arr)
            
        return counter.most_common(1)[0][0]

