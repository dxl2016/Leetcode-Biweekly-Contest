class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        if not prices:
            return 
        ans = []
        for i in range(len(prices)):
            j=i+1
            flag = 0
            while(j<len(prices)):
                if prices[j] <= prices[i]:
                    ans.append(prices[i]-prices[j])
                    flag = 1
                    break
                else:
                    j+=1
            if flag == 0:
                ans.append(prices[i])
        return ans
