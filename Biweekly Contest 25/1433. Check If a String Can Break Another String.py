class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        temp1 = []
        temp2 = []
        n = len(s1)
        for s in s1:
            temp1 += [ord(s)-ord('a')]
        for s in s2:
            temp2 += [ord(s)-ord('a')]
        temp1 = sorted(temp1)
        temp2 = sorted(temp2)
        return (all(temp1[i]>=temp2[i] for i in range(n)) or all(temp1[i]<=temp2[i] for i in range(n)))
