class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        if not words:
            return []
        words = sorted(words, reverse=False, key=lambda x:len(x))
        ans = []
        for i in range(0, len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans

