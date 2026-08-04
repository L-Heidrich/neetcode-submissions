import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ","")

        beg = 0
        end = len(s) - 1

        while(beg < end):

            while(not(s[beg].isalnum()) and beg < end ):
                beg+= 1
            
            while(not(s[end].isalnum()) and beg < end ):
                end-= 1
            
            if(s[beg] != s[end]):
                return False

            beg+= 1
            end-= 1

        return True
