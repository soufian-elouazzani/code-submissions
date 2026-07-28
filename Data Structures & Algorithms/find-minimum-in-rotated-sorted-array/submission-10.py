class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if nums is None:
        #     return None
        # for i in range(len(nums)-1):
        #     if nums[i+1] < nums[i]:
        #         return nums[i+1]
        # return nums[0] 
        i, j = 0, len(nums)-1
        while i < j:
            mid = (i + j) // 2
            if nums[j] < nums[mid]:
                i = mid + 1
            else:
                j = mid
        return nums[i]

                