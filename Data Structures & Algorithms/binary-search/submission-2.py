class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        l = 0
        while l <= r  :
            m = int( (l + r) / 2 )

            if target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
            else :
                return m 

        return -1