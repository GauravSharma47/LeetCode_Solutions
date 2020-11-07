class Solution:
    def countAndSay(self, n: int) -> str:
        temp="1"
        while n-1:
            s=temp+"$"
            temp=""
            count=1
            for i in range(len(s)-1):
                if s[i]==s[i+1]:
                    count+=1
                else:
                    temp+=str(count)+s[i]
                    count=1
            n-=1
        return temp
