class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashNums = {}
        res = [[] for _ in range(len(nums) + 1)]
        final = []
        for num in nums:
            hashNums[num] = 1 + hashNums.get(num, 0)

        for item in hashNums:
            res[hashNums[item]].append(item)
        
        for i in range(len(res)-1, 0, -1):
            for num in res[i]:
                final.append(num)
                if len(final)==k:
                    return final

        return final