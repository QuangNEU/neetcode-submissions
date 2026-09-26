class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # Mảng ảo trải dài từ 0 đến (Tổng số phần tử - 1)
        left = 0
        right = ROWS * COLS - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Dịch tọa độ ảo 1D sang tọa độ thực 2D
            r = mid // COLS
            c = mid % COLS
            mid_val = matrix[r][c]
            
            if mid_val == target:
                return True
            elif mid_val > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False