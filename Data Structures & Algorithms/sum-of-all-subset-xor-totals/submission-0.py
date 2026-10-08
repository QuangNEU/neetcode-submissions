class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, current):
            if i == len(nums):
                return current
            
            take = dfs(i+1, current^nums[i])

            skip = dfs(i+1, current)

            return take+skip
        return dfs(0,0)