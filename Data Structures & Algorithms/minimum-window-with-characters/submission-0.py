class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        t_dict = {}
        window= {}
        left = 0
        have = 0
        res = [-1,-1]
        res_len = float("infinity")
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        need = len(t_dict)
        
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0)+1

            if char in t_dict and window[char] == t_dict[char]:
                have+=1
            
            while(have == need):
                current = right - left +1
                if current < res_len:
                    res = [left, right]
                    res_len = current
                
                left_char = s[left]
                window[left_char] -= 1
                if left_char in t_dict and window[left_char] < t_dict[left_char]:
                    have -= 1
                left +=1
        l, r = res
        return s[l:r+1] if res_len != float("infinity") else ""