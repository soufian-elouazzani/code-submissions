class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = 0
        longest_sub = 0

        for j in range(len(s)):
            # Shrink window from the left until s[j] is unique
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            
            # Add current char and update max length
            seen.add(s[j])
            longest_sub = max(longest_sub, j - i + 1)

        return longest_sub

            

        return longest_sub
        