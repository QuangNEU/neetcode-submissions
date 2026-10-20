class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
            
        target = total / k
        nums.sort(reverse=True)
        
        if nums[0] > target:
            return False
            
        used = [False] * len(nums)
        
        def backtrack(i, k_left, current_sum):
            if k_left == 1:
                return True
                
            if current_sum == target:
                return backtrack(0, k_left - 1, 0)
                
            for j in range(i, len(nums)):
                if not used[j] and current_sum + nums[j] <= target:
                    if j > 0 and not used[j-1] and nums[j] == nums[j-1]:
                        continue
                        
                    used[j] = True
                    if backtrack(j + 1, k_left, current_sum + nums[j]):
                        return True
                    used[j] = False 
                    if current_sum == 0:
                        break
                        
            return False
            
        return backtrack(0, k, 0)