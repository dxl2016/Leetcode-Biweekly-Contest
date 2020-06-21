class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        if not target:
            return
        ans = []
        temp = []
        for i in range(1, n+1):
            if i in target:
                temp.append(i)
                ans.append("Push")
            else:
                ans += ["Push", "Pop"]
            
            if temp == target:
                return ans

