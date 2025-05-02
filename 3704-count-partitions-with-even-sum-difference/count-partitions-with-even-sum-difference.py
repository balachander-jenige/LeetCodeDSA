class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
        for i in range(len(nums)-1):
            if (nums[i]-(nums[len(nums)-1]-nums[i]))%2==0:
                count+=1
        return count

        