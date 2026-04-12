class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, path):
            if sum(path) >= target or i >= len(nums):
                if sum(path) == target :
                    res.append(path.copy())
                return

            path.append(nums[i])
            dfs(i, path)
            path.pop()
            dfs(i+1, path)

            
        dfs(0, [])
        return res