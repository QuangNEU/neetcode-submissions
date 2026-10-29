class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        if k == 0:
            return
        count = 0     
        start = 0    
        while count < n:
            current_idx = start
            prev_val = nums[start]
            while True:
                next_idx = (current_idx + k) % n
                nums[next_idx], prev_val = prev_val, nums[next_idx]
                current_idx = next_idx
                count += 1
                if start == current_idx:
                    break
            start += 1