class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        product_left = 1
        
        for i, j in enumerate(nums):
            
            product_right = 1

            for n in nums[i+1:]:
                product_right = product_right * n
            
            result.append(product_right * product_left)
            product_left = product_left * j

        return result

