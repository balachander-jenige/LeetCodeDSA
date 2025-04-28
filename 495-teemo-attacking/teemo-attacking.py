class Solution:
    def findPoisonedDuration(self, nums: List[int], duration: int) -> int:
        res=0
        for i in range(len(nums)):
            if   i < len(nums)-1 and nums[i+1]-nums[i]<=duration:
                res=res+(nums[i+1]-nums[i])
            else:
                res=res+duration
        return res