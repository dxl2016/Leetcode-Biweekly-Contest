class Solution:
    def maxDiff(self, num: int) -> int:
        if num < 10:
            return 8
        s = str(num)
        n = len(s)
        if all(s[i] == '1' for i in range(n)):
            return '8'*n
        
        if s[0] == '9':
            for flag in s[1:]:
                if flag != '9':
                    break
            s1 = s.replace(flag, '9')
        elif s[0] != '9':
            s1 = s.replace(s[0], '9')
        
        if s[0] != '1':
            s2 = s.replace(s[0], '1')
        elif s[0] == '1' and int(s[1:]) == 0:
            s2 = s
        elif s[0] == '1' and int(s[1:]) > 0:
            for flag1 in s[1:]:
                if flag1 != '0':
                    break
            if flag1 != '1':
                s2 = s.replace(flag1, '0')
            else:
                for flag2 in s[1:]:
                    if flag2 != '0' and flag2 != '1':
                        break
                s2 = s.replace(flag2, '0')

        return abs(int(s1)-int(s2))
    
    
    
