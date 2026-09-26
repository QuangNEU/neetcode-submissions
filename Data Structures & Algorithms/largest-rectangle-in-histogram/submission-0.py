class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        res = 0
        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                popped_idx = stack.pop()
                h = heights[popped_idx]
                left_idx = stack[-1] if stack else -1
                w = i - left_idx - 1
                res = max(res, h*w)
            stack.append(i)
        return res