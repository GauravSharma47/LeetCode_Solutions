class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a=dict([(value,key) for key,value in enumerate(nums)])
        if target in nums:
            return a[target]
        else:
            return -1
