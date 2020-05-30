class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if not arr or not target:
            return True
        n1, n2 = len(target), len(arr)
        if n2 > n1:
            return False
        temp1 = {}
        temp2 = {}
        for i in target:
            try:
                temp1[i] += 1
            except:
                temp1[i] = 1
        for j in arr:
            try:
                temp2[j] += 1
            except:
                temp2[j] = 1
        
        for k in temp1:
            if k not in temp2:
                return False
            if temp1[k] != temp2[k]:
                return False
        return True
    
    
    
