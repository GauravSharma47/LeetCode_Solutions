class Solution:
    def romanToInt(self, s: str) -> int:
        sums=0
        skip=False
        for i in range(len(s)):
            if skip:
                skip=False
                continue
            if i!=len(s)-1:
                if s[i]=="I" and s[i+1]=="V":
                    sums+=4
                    skip=True
                elif s[i]=="I" and s[i+1]=="X":
                    sums+=9
                    skip=True
                elif s[i]=="X" and s[i+1]=="L":
                    sums+=40
                    skip=True
                elif s[i]=="X" and s[i+1]=="C":
                    sums+=90
                    skip=True
                elif s[i]=="C" and s[i+1]=="D":
                    sums+=400
                    skip=True
                elif s[i]=="C" and s[i+1]=="M":
                    sums+=900
                    skip=True
            if skip!=True:
                if s[i]=="M":
                    sums+=1000
                elif s[i]=="I":
                    sums+=1
                elif s[i]=="V":
                    sums+=5
                elif s[i]=="X":
                    sums+=10
                elif s[i]=="L":
                    sums+=50
                elif s[i]=="C":
                    sums+=100
                elif s[i]=="D":
                    sums+=500
                elif s[i]=="V":
                    sums+=1000
        return sums
