from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1
        rightMax = height[right]

        leftMax = height[left]
        summation = 0

        while left < right:

            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                summation += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                summation += rightMax - height[right]

        return summation