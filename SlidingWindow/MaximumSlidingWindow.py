import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        from collections import deque

        left = 0
        res = []
        right = 0
        q = collections.deque()

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            
            q.append(right)

            if left > q[0]:
                q.popleft()
            
            if (right + 1) >= k:
                res.append(nums[q[0]])
                left += 1
            right += 1

        return res





