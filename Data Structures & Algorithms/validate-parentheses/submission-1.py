class Solution:
    def isValid(self, s: str) -> bool:
        data = []
        for i in s:
            if i == '(':
                data.append('(')
            elif i == '{':
                data.append('{')
            elif i == '[':
                data.append('[')
            elif len(data) > 0:
                if i == ')' and data.pop() != '(':
                    return False
                elif  i == ']' and data.pop() != '[':
                    return False
                elif i == '}' and data.pop() != '{':
                    return False
            else:
                return False
        if len(data)!=0:
            return False
        return True