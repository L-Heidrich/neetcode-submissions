class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        record = {}

        product = 0
        
        for i, j in enumerate(nums):

            numss_1 = nums[:i]
            numss_2 = nums[i+1:]
            n_nums = numss_1 + numss_2

            product = 1
            for n in n_nums:
                product = product * n
            
            result.append(product)


            
        return result

