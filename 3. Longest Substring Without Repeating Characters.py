class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=1
        l=len(s)
        if l==1:
            return 1
        max1=0
        while j<l+1:
            c=s[i:j]
            m=len(c)
            if len(set(c))==m:
                max1=max(max1,m)
                j=j+1
            else:
                i=i+1

        return max1
            
