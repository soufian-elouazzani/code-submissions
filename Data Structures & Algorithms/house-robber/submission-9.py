class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # max_robed = 0
        # stored_value = {}
        
        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     if i in stored_value:
        #         return  stored_value[i]
        #     stored_value[i] =  max(nums[i] + dfs(i-2), dfs(i-1))
        #     return stored_value[i]
            
        # return dfs(n-1)
        
        a = 0
        b = 0
        for n in nums:
            max_robed = max(a + n, b)
            a = b
            b = max_robed
        return b