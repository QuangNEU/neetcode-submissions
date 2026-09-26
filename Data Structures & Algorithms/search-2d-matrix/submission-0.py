class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        combine = []
        left = 0
        
        for arr in matrix:
            combine += arr
        right = len(combine)-1
        while(left <= right):
            mid = (right + left)//2
            if combine[mid] == target:
                return True
            elif combine[mid] > target:
                right = mid -1
            else:
                left = mid +1
        return False