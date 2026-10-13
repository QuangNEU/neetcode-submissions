class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums) # Mảng đánh dấu các vị trí đã dùng

        def dfs(permutate):
            if len(permutate) == len(nums):
                res.append(permutate.copy())
                return
            
            for i in range(len(nums)):
                if used[i]: 
                    continue
                    
                used[i] = True 
                permutate.append(nums[i])
                
                dfs(permutate)
                
                permutate.pop()
                used[i] = False 

        dfs([])
        return res