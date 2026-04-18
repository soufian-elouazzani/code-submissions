class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def solve(arr):  
            n = len(arr)
            dp = [-1] * n
            
            def dfs(i):
                if i >= n:
                    return 0
                if dp[i] != -1:
                    return dp[i]
                
                dp[i] = arr[i] + max(dfs(i+2), dfs(i+3))
                return dp[i]
            
            return max(dfs(0), dfs(1))
        
        # Two scenarios
        scenario1 = solve(nums[1:])   # Exclude first house
        scenario2 = solve(nums[:-1])  # Exclude last house
        
        return max(scenario1, scenario2)
