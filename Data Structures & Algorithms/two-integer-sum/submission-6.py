class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, _ in enumerate(nums): 
            for x, _ in enumerate(nums): 
                if x == i:
                    continue
                if nums[i] + nums[x] == target:
                    return [i, x]