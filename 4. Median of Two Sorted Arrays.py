class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)
        if  n%2!=0:
            result=nums1[(n//2)]
        else:
            result=(nums1[n//2]+nums1[(n//2)-1])/2
        return result
        
