class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        if not reservedSeats:
            return
        tmp = {}
        for (x,y) in reservedSeats:
            if x not in tmp:
                tmp[x] = [y]
            else:
                tmp[x] += [y]
        c = 0
        a = [[2,3,4,5],[4,5,6,7],[6,7,8,9]]
        q = 0
        for items in tmp:
            q += 1
            b = [1,1,1]
            for j in tmp[items]:
                if 2<=j<=5:
                    if j<4:
                        b[0] = 0
                    else:
                        b[0] = b[1] = 0
                elif 6<=j<=9:
                    if j>7:
                        b[2] = 0
                    else:
                        b[1] = b[2] = 0
                        
            if b[1] == 0:
                c += sum(b)
            else:
                if sum(b) == 1:
                    c += 1
                else:
                    c += sum(b)-1
                    
            # print(b)     
        return c + 2*(n-q)

