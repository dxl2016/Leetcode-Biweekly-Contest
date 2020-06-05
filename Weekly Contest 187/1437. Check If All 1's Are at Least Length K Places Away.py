class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if not nums:
            return True
        space = float('Inf')
        for i in nums:
            if i == 1:
                if space < k:
                    return False
                space = 0
            else:
                space += 1
        return True
