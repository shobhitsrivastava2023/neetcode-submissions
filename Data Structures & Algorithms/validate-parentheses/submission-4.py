class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brack = ['(', '{', '[']
        close_brack = [')', '}', ']']

        for char in s: 
            if char in open_brack: 
                stack.append(char)
            elif char in close_brack: 
                if not stack or stack[-1] != open_brack[close_brack.index(char)]: 
                    return False 
                else: 
                    stack.pop() 
        
        return len(stack) == 0
            

        