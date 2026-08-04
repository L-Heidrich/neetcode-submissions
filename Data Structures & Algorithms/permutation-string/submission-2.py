class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        char_counts_s1 = {}
        l = 0

        for char in s1:
            char_counts_s1[char] = char_counts_s1.get(char, 0) + 1

        for r in range(len(s2)):
            char_counts_window = {}

            if s2[r] not in s1:
                l+=1
                continue

            for char in s2[l:l+len(s1)]:
                char_counts_window[char] = char_counts_window.get(char, 0) + 1

            if char_counts_window == char_counts_s1:
                return True 
            else: 
                l+=1
        
        return False
            

            
            