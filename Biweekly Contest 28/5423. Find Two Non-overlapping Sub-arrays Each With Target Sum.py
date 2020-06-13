class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        if not arr:
            return 0
        if sum(arr) <= target:
            return -1
        
        temp = []
        l = [0]
        cusum = 0
        for i in arr:
            cusum += i
            l.append(cusum)
        n = len(l)
        for i in range(0, n):
            for j in range(i, n):
                if l[j]-l[i] == target:
                    try:
                        temp += [(j-i,i,j-1)]
                    except:
                        temp = [(j-i,i,j-1)]
        temp = sorted(temp, reverse=False, key=lambda x:x[0])
        # print(temp)
        global_min = float('Inf')
        for i in range(0, len(temp)):
            for j in range(i+1, len(temp)):
                curr_val = temp[i][0] + temp[j][0]
                if curr_val >= global_min:
                    break
                
                if min(temp[i][2], temp[j][2]) < max(temp[i][1], temp[j][1]):
                    if curr_val < global_min:
                        global_min = curr_val
                        
        return global_min if global_min < float('Inf') else -1
        
