class Solution:
    def isPalindrome(self, s: str) -> bool:
        pure_str = ''.join(char for char in s.lower() if char.isalnum())
        return pure_str == pure_str[::-1]