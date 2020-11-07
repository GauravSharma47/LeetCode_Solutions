class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i=0
        while i<len(arr):
            if arr[i]*2 in arr:
                if arr[i]==0:
                    if arr.count(0)>1:

                        return True
                    else:
                        i+=1
                        continue
                return True
            i+=1

        return False
        
