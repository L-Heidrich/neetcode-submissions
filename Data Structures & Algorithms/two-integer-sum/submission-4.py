class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, j in enumerate(nums): 
            for x, c in enumerate(nums): 
                if j + c == target:
                    if x == i:
                        continue
                    return [i, x]