class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # BƯỚC 1: Bắt buộc sắp xếp để các số giống nhau đứng cạnh nhau
        candidates.sort()
        res = []

        def dfs(i, current_sum, subset):
            if current_sum == target:
                res.append(subset.copy()) 
                return
            
            if current_sum > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                subset.append(candidates[j])
                dfs(j + 1, current_sum + candidates[j], subset)
                subset.pop()

        dfs(0, 0, [])
        return res