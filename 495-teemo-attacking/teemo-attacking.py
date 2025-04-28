class Solution:
    def findPoisonedDuration(self, nums: List[int], duration: int) -> int:
        res=0
        for i in range(len(nums)-1):
            res+=min(duration,nums[i+1]-nums[i])
        res+=duration
        return res