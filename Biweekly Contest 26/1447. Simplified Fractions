class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def commonGCD(r, i):
            while i != 0:
                (r, i) = (i, r % i)
            return r

        temp = []
        if n == 1:
            return temp
        for i in range(2, n+1):
            temp.append('1/'+str(i))
        r = 2
        while (r<n):
            for i in range(r, n+1):
                if commonGCD(r, i) == 1 and r < i:
                    temp.append(str(r)+'/'+str(i))
            r += 1
        return temp
            
