class Solution:
    def leftRightDifference(self, nums):
        n = len(nums)
        ans = [0] * n
        total_sum = sum(nums)
        left_sum = 0

        for i in range(n):
            right_sum = total_sum - left_sum - nums[i]
            ans[i] = abs(left_sum - right_sum)
            left_sum += nums[i]

        return ans