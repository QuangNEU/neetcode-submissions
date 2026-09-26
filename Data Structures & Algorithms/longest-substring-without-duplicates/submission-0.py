class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res =0 
        count = 0
        left = 0
        for i in range(len(s)):
            count+=1
            while s[i] in s[left:i]:
                left+=1
                count-=1
            res = max(res, count)
        return res