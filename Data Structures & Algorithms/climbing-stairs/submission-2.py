class Solution:
    def climbStairs(self, n: int) -> int:
        # Direct solution
        #  res = 0
        # stored_data = []
        # def rec(n, res):
        #     if res in stored_data:

        #     if res == n:
        #         return 1
        #     if res > n :
        #         return 0
        #     return rec(n,res+1) + rec(n,res+2)

        # return rec(n,res+1) + rec(n,res+2)
        if n == 1 :
            return 1
        elif n == 2:
            return 2
            
        b = 1
        c = 1
        for i in range(n-1):
            temp = b
            b = b + c 
            c = temp
        return b
