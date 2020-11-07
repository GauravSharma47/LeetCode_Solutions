class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        i=0
        while i<len(nums)-2:
            if i==0 or nums[i]!=nums[i-1]:
                l=i+1
                r=len(nums)-1
                sums=0-nums[i]
                while l<r:
                    ln=nums[l]
                    rn=nums[r]
                    if ln+rn>sums:
                        r=r-1
                    elif ln+rn<sums:
                        l=l+1
                    else:
                        res.append([nums[i],ln,rn])
                        l+=1
                        r-=1
                        while r>0 and nums[r]==rn:
                            r-=1
                        while l<len(nums)-1 and nums[l]==ln:
                            l+=1
            i+=1
        return res

               
