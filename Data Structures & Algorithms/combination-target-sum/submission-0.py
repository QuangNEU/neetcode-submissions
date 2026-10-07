class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, current_sum, subset):
            if current_sum == target:
                res.append(subset.copy())
                return
                
            if current_sum > target or i >= len(candidates):
                return
                
            subset.append(candidates[i])
            dfs(i, current_sum + candidates[i], subset)
            
            subset.pop() 
            dfs(i + 1, current_sum, subset)
            
        dfs(0, 0, [])
        return res