class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest_substring = 0
        i = 0
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i+=1

            seen.add(s[j])
            longest_substring = max(longest_substring, j-i+1)
        return longest_substring