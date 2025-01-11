from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_set = defaultdict(int)
        num_list = [[] for i in range(len(nums) + 1)]

        for i in nums:
            if i in num_set:
                num_set[i] += 1
            else:
                num_set[i] = 1
        
        for j, v in num_set.items(): 
            num_list[v].append(j)

        res = []

        for i in range(len(num_list) - 1, 0, -1):
            for j in num_list[i]:
                res.append(j)
                if len(res) == k:
                    return res