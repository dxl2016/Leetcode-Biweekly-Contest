class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        def check_subset(lng, shrt):
            count_lng = collections.Counter(lng) 
            count_shrt = collections.Counter(shrt) 
            
            for key in count_shrt: 
                if key not in count_lng: 
                    return False
                if count_shrt[key] > count_lng[key]: 
                    return False
            return True
        
        ans = [x for x in range(len(favoriteCompanies))]
        for i in range(len(favoriteCompanies)):
            for j in range(len(ans)):
                if i != ans[j]:
                    if check_subset(favoriteCompanies[ans[j]], favoriteCompanies[i]):
                        ans.remove(i)
                        break
        return ans
                
                
                
                
            
        
