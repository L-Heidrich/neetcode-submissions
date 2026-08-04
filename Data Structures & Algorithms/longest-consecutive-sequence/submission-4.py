class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # [2, 20, 4, 10, 3, 4, 5]
        # 

        visited = set(nums)
        sequences = [0]
        
        for n in nums:
            if n+1 not in visited:   
                i = n
                s = 0
                
                while i in visited:
                    s+=1
                    i -= 1
                sequences.append(s)

        return max(sequences)
                

            

            