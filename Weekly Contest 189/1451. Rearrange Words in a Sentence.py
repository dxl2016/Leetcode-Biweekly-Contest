class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split()
        temp = {}
        for txt in text:
            try:
                temp[len(txt)] += [txt.lower()]
            except:
                temp[len(txt)] = [txt.lower()]
        temp = sorted(temp.items(), reverse=False)
        flag = 0
        for items, val in temp:
            for j in val:
                if flag == 0:
                    ans = j.capitalize() + ' '
                    flag = 1
                else:
                    ans += (j + ' ')
        return ans[:-1]
