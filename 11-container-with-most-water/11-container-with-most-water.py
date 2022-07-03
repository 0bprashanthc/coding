class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        left, right = 0, size - 1
        maxArea = 0
        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width
            maxArea = max(maxArea, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxArea