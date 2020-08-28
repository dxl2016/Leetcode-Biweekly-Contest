class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:       
        def dfs(idx, seen):
                curr_max_val, curr_max_idx = 0, []
                flag = 0
                for i in range(idx+1, idx+d+1):
                    if 0<=i<n and arr[i]<arr[idx]:
                        if i not in seen and arr[i]>=curr_max_val:
                            curr_max_val = arr[i]
                            curr_max_idx.append(i)
                            flag = 1
                    else:
                        break
                if flag == 1:
                    for each in curr_max_idx:
                        dfs(each, seen+[each])
                else:
                    self.ans = max(self.ans, len(seen))
                
                curr_max_val, curr_max_idx = 0, []
                flag = 0
                for j in range(idx-1, idx-d-1, -1):
                    if 0<=j<n and arr[j]<arr[idx]:
                        if j not in seen and arr[j]>=curr_max_val:
                            curr_max_val = arr[j]
                            curr_max_idx.append(j)
                            flag = 1
                    else:
                        break
                if flag == 1:
                    for each in curr_max_idx:
                        dfs(each, seen+[each])
                else:
                    self.ans = max(self.ans, len(seen))
        
        self.ans = 0
        n = len(arr)
        print(n)
         
        for idx,_ in enumerate(arr):
            seen = []
            dfs(idx, seen+[idx])
        
        return self.ans

