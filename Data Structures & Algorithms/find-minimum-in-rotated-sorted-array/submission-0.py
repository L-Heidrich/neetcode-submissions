class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums) -1
        l = 0
        r = n

        while l < r: 
            mid = (l + r) // 2

            if nums[mid] > nums[r]: # if right is bigger, the rise of numbers must be to the right
                l = mid+1                   

            elif nums[mid] < nums[r]:
                r = mid                   

        return nums[l]