from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        n = len(nums)
        if n == 0 and target != 0:
            return 0
        elif target == sum(nums):
            return len(nums)
        elif target > sum(nums):
            return 0
        for i in range(n):
            sum1 = nums[i]
            cnt = 1
            if sum1 >= target:
                return cnt
            for j in range(i+1, n):
                sum1 += nums[j]
                cnt += 1
                if sum1 >= target:
                    return cnt
        return 0
