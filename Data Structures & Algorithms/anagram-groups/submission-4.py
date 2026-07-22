class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_holder = defaultdict(list)
        list_holder = [0] * 26
        for elem in strs :
            # sorted_elem = "".join(sorted(elem)) 
            for letter in elem:
                list_holder[ord(letter) - ord("a")] += 1
            hashableitem = tuple(list_holder)  
            list_holder = [0] * 26
            # placeholder[sorted_elem].append(elem)
            dict_holder[hashableitem].append(elem)
        return list(dict_holder.values())