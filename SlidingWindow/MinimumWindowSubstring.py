from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        

        window_map = defaultdict(int)
        t_freq = defaultdict(int)
        
        have = 0
        

        for i in t:
            t_freq[i] = 1 + t_freq.get(i, 0)
        
        need = len(t_freq)
        res = [-1, -1]
        res_length = float("inf")
        left = 0

        for right in range(len(s)):
            
            char = s[right]
            window_map[char] = 1 + window_map.get(char, 0)

            if char in t_freq and window_map[char] == t_freq[char]:
                have += 1
            
            while have == need:
                if (right - left + 1) < res_length:
                    res = [left, right]
                    res_length = (right - left + 1)
                
                window_map[s[left]] -= 1

                if s[left] in t_freq and window_map[s[left]] < t_freq[s[left]]:
                    have -= 1
                left += 1
            
        l, r = res
            
        if res_length != float("inf"):
            return s[l:r+1] 

        return ""