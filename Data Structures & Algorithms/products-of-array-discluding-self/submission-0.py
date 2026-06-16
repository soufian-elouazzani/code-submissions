class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # total = 1
        # indexs = []
        # for j in range(len(nums)):
        #     if nums[j] != 0 :
        #         total *= nums[j]
        #     else : 
        #         indexs.append(j)
            
        # if len(indexs) >= 2 :
        #     return [ 0 ] * len(nums)
        # if len(indexs) == 1 :
        #     new_list = [ 0 ] * len(nums)  
        #     new_list[indexs[0]] = total
        #     return new_list

        # for j in range(len(nums)):
        #     nums[j] = int(total/nums[j])
             
        # return nums
        n = len(nums)
        res = [1] * n
        
        # Step 1: Calculate the prefix products (everything to the left)
        # res[i] will store the product of all numbers before index i
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate the suffix products (everything to the right)
        # Multiply the existing prefix products by the suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res