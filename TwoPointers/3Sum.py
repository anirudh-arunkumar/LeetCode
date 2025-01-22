from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):

            if i > 0 and val == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = val + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
    
        return res