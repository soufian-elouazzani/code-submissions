class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_consec = 0
        for num in nums :
            if num - 1 not in nums_set:
                i = 0
                while num + i in nums_set:
                    i += 1

                max_consec = max(max_consec, i)
        
        return max_consec

