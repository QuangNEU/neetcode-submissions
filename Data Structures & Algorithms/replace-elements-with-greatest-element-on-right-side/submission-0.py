class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1
        
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = current_max
            if temp > current_max:
                current_max = temp
        return arr