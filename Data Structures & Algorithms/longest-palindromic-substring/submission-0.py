class Solution:
    def longestPalindrome(self, s: str) -> str:
        # #Btute force Solution:
        # n = len(s)
        # longestPal = ""
        # for i in range(n-1):
        #     for j in range(i, n):
        #         newcandidat = s[i:j]
        #         flag = True
        #         for k in range(len(newcandidat)/2):
        #             if newcandidat[k] != newcandidat[len(newcandidat)-1]:
        #                 flag = False
        #                 break
        #         if flag and len(newcandidat) > len(longestPal):
        #             longestPal = newcandidat
        

                    
        # def helper(s:str):
        #     for i in range(int(len(s)/2)):
        #         if s[i] != s[n-1-i]:
        #             return False
        #     return True

        # dp = [-1]*len(s)
        # def dfs(s):
        #     if s == "":
        #         return 0

        #     if self.helper(s) == False:
        #         dp[i] = max(dfs(s[1:]), dfs(s[:1]))
        #     else:
        #         return len(s)
        #     return dp[i]
        # return dfs(s)
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        result = ""
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i+1)
            
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
        
        return result

            
        
            
