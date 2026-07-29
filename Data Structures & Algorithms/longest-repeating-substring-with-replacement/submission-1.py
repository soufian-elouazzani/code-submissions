class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        track_letters = defaultdict(int)
        i = 0
        most_freq_in_window = 0
        longest_chain = 0
        for j in range(len(s)):
            track_letters[s[j]] += 1
            most_freq_in_window = max(most_freq_in_window, track_letters[s[j]])
            window = j - i + 1
            if window - most_freq_in_window <=  k :
                longest_chain = max(longest_chain, window)
                
            else:
                track_letters[s[i]] -= 1
                i += 1
             
                
        return longest_chain
        
                
