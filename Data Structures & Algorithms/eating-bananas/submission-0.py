class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = (sum(piles)+h-1)//h
        left = max(1,left)
        right = max(piles)
        while left <= right:
            k = (right+left)//2
            total_hour = 0
            for pile in piles:
                total_hour += (pile+k-1)//k
                if total_hour > h:
                    break
            if total_hour <= h:
                res = k
                right = k-1
            else:
                left = k +1
        return res