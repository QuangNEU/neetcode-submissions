class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(permutate):
            if len(permutate) == len(nums):
                res.append(permutate.copy())
                return
            for i in range(len(nums)):
                if nums[i] in permutate:
                    continue
                permutate.append(nums[i])
                dfs(permutate)
                permutate.pop()
        dfs([])
        return res           