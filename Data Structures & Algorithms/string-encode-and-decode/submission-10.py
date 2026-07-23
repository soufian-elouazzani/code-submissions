class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res += str(len(s)) + ":" + s 
        return res 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != ":":
                j += 1
            
            length = int(s[i:j])
            
            start_of_str = j + 1
            end_of_str = start_of_str + length
            res.append(s[start_of_str:end_of_str])
            
            i = end_of_str
            
        return res