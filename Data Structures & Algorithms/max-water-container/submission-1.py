class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right: 
            
            a = heights[left]
            b = heights[right]

            if a < b: 
                area = a * (right -left)
                left+=1
            else: 
                area = b * (right - left) 
                right-=1
            if area > max_area:
                max_area = area

        return max_area

    
        

            

