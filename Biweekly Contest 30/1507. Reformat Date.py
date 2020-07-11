class Solution:
    def reformatDate(self, date: str) -> str:
        if not date:
            return ""
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        day_end = ["st", "nd", "rd", "th"]
        s = date.split()
        for i in range(len(month)):
            if s[1] == month[i]:
                idx = i+1
                break
        if len(str(idx)) == 1:
            l = "0"+str(idx)
        else:
            l = str(idx)
        if len(s[0][:-2]) == 1:
            m = "0"+s[0][:-2]
        else:
            m = s[0][:-2]
        return s[2]+"-"+l+"-"+m

