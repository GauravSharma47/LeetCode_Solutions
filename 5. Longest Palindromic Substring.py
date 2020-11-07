class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<2:
            return s
        high=0
        cur=""
        for i in range(n):
            for j in range(i,n):
                a=s[i:j+1]
                if a==a[::-1] and len(a)>high:
                    cur=a
                    high=len(a)
        return cur

                
