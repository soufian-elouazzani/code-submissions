class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def rob_stright_house(lst):
            a, b = 0,0 
            for num in lst :
                place_holder = max(a + num, b)    
                a = b
                b = place_holder
            return b

        return max(rob_stright_house(nums[:-1]), rob_stright_house(nums[1:]) )