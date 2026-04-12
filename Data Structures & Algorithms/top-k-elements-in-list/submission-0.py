class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {} 
        list_max = [0] * k
        res = []
        for num in nums :
            nums_dict[num] = nums_dict.get(num, 0) + 1
        ordered_freq = sorted(nums_dict.values())
        ordered_freq = ordered_freq[len(ordered_freq)-k::]
        for value in nums_dict :
            if nums_dict[value] in ordered_freq:
                res.append(value)
        
        return res
