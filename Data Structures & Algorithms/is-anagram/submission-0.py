class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_of_s = list(s)
        list_of_t = list(t)

        return sorted(list_of_t) == sorted(list_of_s) 