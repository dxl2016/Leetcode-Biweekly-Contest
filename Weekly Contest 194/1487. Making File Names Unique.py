class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        tmp = {}
        for x in names:
            if x not in ans:
                if x[-1] != ")":
                    ans.append(x)
                    tmp[x] = [0]
                else:
                    ans.append(x)
                    tmp[x] = [0]
                    xl = x.split("(")
                    if xl[0] in tmp:
                        tmp[xl[0]] += [int(xl[1][:-1])]
                    else:
                        tmp[xl[0]] = [int(xl[1][:-1])]  
            else:
                i = 0
                while(True):
                    if i in tmp[x]:
                        i += 1
                    else:
                        tmp[x] += [i]
                        break
                    
                ans.append(x+"("+str(i)+")")
        return ans

