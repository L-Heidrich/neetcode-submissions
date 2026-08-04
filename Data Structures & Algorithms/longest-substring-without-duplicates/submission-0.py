class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window_size = 0
        sett = set()
        n = len(s)
        left = 0 
        longest = 0

        for i in range(n):
            while s[i] in sett:
                sett.remove(s[left])
                left += 1
            
            sett.add(s[i])
            longest = max(longest, (i - left) + 1 )

        return longest 


                



