class Solution:
    def climbStairs(self, n: int) -> int:
        stored_results = {}        
        if n < 2:
            return 1

        def dfs(num):
            if num == 0:
                return 1
            if num < 0:
                return 0

            if num in stored_results:
                return stored_results[num]

            stored_results[num] = dfs(num-1) + dfs(num-2)

            return stored_results[num]

        return dfs(n)



