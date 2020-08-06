from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date_format = "%Y-%m-%d"
        a = datetime.strptime(date1, date_format)
        b = datetime.strptime(date2, date_format)
        delta = b-a
        
        return abs(delta.days)

