class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_surface=0
        i,j=0,len(heights)-1
        while i < j:
            surface=min(heights[i],heights[j]) * (j-i)
            if surface > max_surface:
                    max_surface = surface
            if heights[i] < heights[j]:
                i+=1
            else :
                j-=1 
        return max_surface