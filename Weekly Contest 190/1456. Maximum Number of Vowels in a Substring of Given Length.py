class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return
        dict_vowel = ['a', 'e', 'i', 'o', 'u']
        if k == 1:
            for i in s:
                if i in dict_vowel:
                    return 1
        n_s = len(s)
        count = 0
        l, r = 0, k
        for i in s[:k]:
            if i in dict_vowel:
                count += 1
        max_count = count
        while(r<n_s):
            if s[l] in dict_vowel:
                count -= 1
            if s[r] in dict_vowel:
                count += 1
            if count > max_count:
                max_count = count
            l += 1
            r += 1
        return max_count
