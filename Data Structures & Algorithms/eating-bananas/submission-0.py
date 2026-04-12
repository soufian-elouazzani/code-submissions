class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # list of possible k = {1,2, ... ,max(piles)}
        
        l,r = 1,max(piles) 
        res = max(piles)

        while l <= r :
            k = (r + l) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / k)

            if hours <= h:
                res = k
                r = k -1
            else:
                l = k + 1

        return res