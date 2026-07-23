class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # count_map = Counter(nums)

        # elems = sorted(count_map.keys(), key=lambda x:count_map[x] , reverse=True)

        # return elems[:k]

        # # second approach
        # import heapq
        # from collections import  Counter

        # count_map = Counter(nums)

        # heap = []

        # for elem, freq in count_map.items():
        #     heapq.heappush(heap, (freq, elem))

        #     if len(heap) > k :
        #         heapq.heappop(heap) 
        # return [elem for (i, elem) in heap]
        count_map = Counter(nums)
        bucket_list = [[] for _ in range(len(nums)+1) ]
        
        for elem, freq in count_map.items():
            bucket_list[freq].append(elem)

        results=[]
        for i in range(len(bucket_list)-1 ,0 , -1):
            for item in bucket_list[i]:
                results.append(item)

                if len(results) == k :
                    return results

        
