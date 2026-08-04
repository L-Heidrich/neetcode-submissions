class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        n = len(s)
        sett = set()
        longest = 0
        counts = [0] * 26

        for r in range(n): 
            counts[ord(s[r]) - 65] += 1

            while (r-l + 1) - max(counts) > k: 
                counts[ord(s[l]) - 65] -= 1
                l +=1

            longest = max((r-l+1), longest)

        return longest
            




            

