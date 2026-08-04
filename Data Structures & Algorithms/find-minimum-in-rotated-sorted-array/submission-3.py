class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums) -1
        l = 0
        r = n

        while l < r: 
            mid = (l + r) // 2

            if nums[mid] > nums[r]: # if mid is bigger than right, it cannot be minimum. rise is to the right, therfore move l to mid, mid is not the minimum, therefore +1
                l = mid+1                   

            elif nums[mid] < nums[r]:
                r = mid                   

        return nums[l]