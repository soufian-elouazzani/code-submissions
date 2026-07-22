class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        placeholder = defaultdict(list)
        for elem in strs :
            sorted_elem = "".join(sorted(elem)) 
            placeholder[sorted_elem].append(elem)
        return list(placeholder.values())