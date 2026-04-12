class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        lstHashMap = {}
        for item in strs:
            counterH = {}
            for letter in item:
                counterH[letter] = 1 + counterH.get(letter, 0) 
            hashCounterH = tuple(sorted(counterH.items())) 
            if hashCounterH in lstHashMap.keys():
                lstHashMap[hashCounterH].append(item)
            else:
                lstHashMap[hashCounterH] = [item]
        
        return list(lstHashMap.values())
