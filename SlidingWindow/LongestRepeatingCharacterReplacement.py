from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        freq = defaultdict(int)

        for r in range(len(s)):
            freq[s[r]] += 1
            maxFreq = max(freq.values())
            curr = r - l + 1

            if curr - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
    
        return res

            