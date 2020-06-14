class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if not arr:
            return 0
        temp = {}
        for i in arr:
            try:
                temp[i] += 1
            except:
                temp[i] = 1
        
        temp = sorted(temp.items(),reverse=True,key=lambda x:x[1])
        diff = k
        while(diff>0 and temp):
            items = temp.pop()
            diff -= items[1]
        if diff == 0:
            return len(temp)
        else:
            return len(temp)+1

