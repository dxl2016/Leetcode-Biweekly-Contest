class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        curr_s = s[0]
        count = 1
        max_count = 1
        for i in s[1:]:
            if curr_s == i:
                count +=1
                if count > max_count:
                    max_count = count
            else:
                if count > max_count:
                    max_count = count
                curr_s = i
                count = 1
        return max_count
            
            
