class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        if not height:
            return 0
            
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        while(left<right):
            if height[left] < height[right]:
                left += 1
                max_left = max(height[left], max_left)
                res += max_left - height[left]
            else:
                right -= 1
                max_right = max(height[right], max_right)
                res+= max_right - height[right]
        return res