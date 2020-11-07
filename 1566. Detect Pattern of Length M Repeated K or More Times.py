class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if len(arr)<m*k:
            return False
        i=0
        l=m*k
        while i<=len(arr)-l:
            if k*arr[i:i+m]==arr[i:i+l]:

                return True
            else:
                i+=1

        return False
