class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        data = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'            
        }
        res = []
        if len(digits) == 0:
            return res
        def dfs(i, letter):
            if len(letter) == len(digits):
                res.append(letter)
                return
            digit = digits[i]
            for char in data[digit]:
                dfs(i+1, letter+char)
            return
        dfs(0, '')
        return res