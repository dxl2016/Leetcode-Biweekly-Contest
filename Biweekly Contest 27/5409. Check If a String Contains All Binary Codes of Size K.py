class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if not s:
            return False
        if not k:
            return True
        n_s = len(s)
        result = set()
        for i in range(0, n_s-k+1):
            result.add(int(s[i:i+k], 2))
        return len(result) == (1<<k)
