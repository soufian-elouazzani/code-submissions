class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None:
            return None
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                return nums[i+1]
        return nums[0] 