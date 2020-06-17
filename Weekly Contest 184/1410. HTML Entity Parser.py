class Solution:
    def entityParser(self, text: str) -> str:
        if not text:
            return ""
        temp = {"&quot": "\"", 
                "&apos": "'",
                "&amp": "&",
                "&gt": ">",
                "&lt": "<",
                "&frasl": "/"};
        ans = ""
        s = text.split(';')
        for items in s[:-1]:
            print(items)
            flag = 0
            for i in temp:
                if i in items:
                    flag = 1
                    items = items.replace(i, temp[i])
                    break
            if flag == 0:
                ans += items + ';'
            else:
                ans += items
        
        return ans+s[-1]
 
 
