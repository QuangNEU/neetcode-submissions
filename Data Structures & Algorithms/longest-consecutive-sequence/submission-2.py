class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in s:
            if num-1 not in s:
                current_num = num
                count = 1
                while(current_num +1 in s):
                    current_num +=1
                    count +=1
                res = max(res, count)
        return res