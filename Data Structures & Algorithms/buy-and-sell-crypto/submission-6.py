class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0

        if len(prices) == 1 :
            return max_prof
        

        i, j = 0, 1
        
        while j < len(prices) :
            if prices[i] >= prices[j] :
                i = j
            max_prof = max(max_prof, prices[j]-prices[i])
            j += 1

        return max_prof