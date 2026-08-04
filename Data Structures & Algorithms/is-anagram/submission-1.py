class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts_s = {}
        counts_t = {}
     
        for i, j in zip(s,t):
            counts_t[i] = counts_t.get(i, 0) + 1
            counts_s[j] = counts_s.get(j, 0) + 1
            
        if counts_t == counts_s: 
            return True
        else:
            return False
        
        
        

        

        
        