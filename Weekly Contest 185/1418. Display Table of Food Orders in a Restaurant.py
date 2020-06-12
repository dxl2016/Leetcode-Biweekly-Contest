class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        if not orders:
            return

        name_dict = set()
        num_dict = set()
        table_dict = {}
        for items in orders:
            if items[2] not in name_dict:
                name_dict.add(items[2])
            if items[1] not in num_dict:
                num_dict.add(items[1])
                table_dict[items[1]] = {}

            try:
                table_dict[items[1]][items[2]] += 1
            except:
                table_dict[items[1]][items[2]] = 1

        result = sorted(table_dict.items(), reverse=False, key=lambda x:int(x[0]))
        print(result)
        name_dict = sorted(name_dict)
        print(name_dict)
        num_dict = sorted(num_dict, reverse=False, key=lambda x:int(x))
        print(num_dict)
        
        temp = []
        while(result):
            t = result.pop(0)
            tt = num_dict.pop(0)
            ans = []
            for items in name_dict:
                if items in t[1]:
                    ans += str(t[1][items])
                else:
                    ans += "0"
            
            temp += [[tt] + ans]
        return([['Table']+name_dict] + temp)
        
        
        
