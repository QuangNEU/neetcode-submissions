class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(par, opened, closed):
            if len(par) == n*2:
               res.append(par)
               return 
            if opened < n:
                dfs(par+'(', opened+1, closed)
            if opened > closed:
                dfs(par+')', opened, closed + 1)
           
        dfs('(', 1, 0)
        return res