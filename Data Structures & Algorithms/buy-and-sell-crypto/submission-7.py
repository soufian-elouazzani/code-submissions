class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_profit = 0
        n = len(prices)
        if n < 2 :
            return 0

        while j  < n:
            if prices[i] >= prices[j]:
                i = j
                j += 1
                continue
            max_profit = max(max_profit, prices[j]-prices[i])
            j +=1
        
        return max_profit
            