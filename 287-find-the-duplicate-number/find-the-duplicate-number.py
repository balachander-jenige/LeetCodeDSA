class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen=set(nums)
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                return num
