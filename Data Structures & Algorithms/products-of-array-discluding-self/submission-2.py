class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        products = []
        
        product_left = 1
        for j in nums:
            result.append(product_left)
            product_left = product_left * j

        product_right = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= product_right
            product_right *= nums[i]
    

            
        return result

