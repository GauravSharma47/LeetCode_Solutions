class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        c=""
        for s in zip(*strs):
            if len(set(s))>1:
                break
            else:
                c+=s[0]

        return c


            
