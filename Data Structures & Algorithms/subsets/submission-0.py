class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            else:
                # decision 1 go right after adding:
                subset.append(nums[i])
                dfs(i+1)
                # decision 2 do left after poping:
                subset.pop()
                dfs(i+1)
                

        dfs(0)
        return res