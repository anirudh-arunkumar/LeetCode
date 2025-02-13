from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        heights.append(0)
        for index, height in enumerate(heights):
            start = index

            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                area = h * (index - i)
                maxArea = max(maxArea, area)
                start = i
            
            stack.append((start, height))
        
        return maxArea