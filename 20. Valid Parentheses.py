class Solution:
    def isValid(self, s: str) -> bool:
        l=['a']
        m={")":"(","}":"{","]":"["}
        for i in s:
            if i in ['(','[','{']:
                l.append(i)
            elif l[-1]==m[i]:
                l.pop()
            else:
                return False
        if len(l)==1:
            return True

        
