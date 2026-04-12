class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNums = {}

        for i,num in enumerate(nums):
            comp = target - num
            if comp in hashNums.keys():
                return [hashNums[comp], i]

            hashNums[num] = i
        return []