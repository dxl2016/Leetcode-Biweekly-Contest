class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        if not rains:
            return
        n = len(rains)
        ans = [1]*n
        q = {}
        q_val = set()
        zeros = deque()
        flag = 0
        
        for k,v in enumerate(rains):
            if v == 0:
                if not q and flag == 0:
                    continue
                elif flag == 1:
                    zeros.append(k)
                    
            else:
                if flag == 0:
                    flag = 1
                
                if v not in q_val:
                    q_val.add(v)
                    q[v] = k
                else:
                    z = q[v]
                    # print(z)
                    for idx in zeros:
                        if idx > z:
                            zeros.remove(idx)
                            ans[z] = -1
                            ans[idx] = v
                            q[v] = k
                            break
                    
                    if z == q[v]:
                        return []
        
        # print(ans)
        for items in q:
            ans[q[items]] = -1
            
        return ans

