class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(start, path):
            if start == len(s):
                res.append(path.copy())
                return
            
            for i in range(start, len(s)):
                substring = s[start:i+1]
                
                if substring == substring[::-1]:
                    path.append(substring)
                    
                    dfs(i + 1, path)
                    
                    path.pop()
                    
        dfs(0, [])
        return res