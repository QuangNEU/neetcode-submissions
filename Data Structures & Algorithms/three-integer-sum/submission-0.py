class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
                
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i+1
            k = len(nums)-1
            target = -nums[i]
            while(j<k):
                total = (nums[j] + nums[k])
                if total == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                elif total < target:
                    j += 1
                else:
                    k -=1
        return res