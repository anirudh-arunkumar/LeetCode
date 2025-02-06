from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

            print(left, mid, right)
        
        return -1