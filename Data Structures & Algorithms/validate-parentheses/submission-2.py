class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        for sign in s:
            if sign in "([{":
                stack.append(sign)

            
           

            elif sign == ")" and stack and stack[-1] == "(":
                stack.pop()
            
          
            elif sign == "]" and stack and  stack[-1] == "[":
                stack.pop()

          
            elif sign == "}" and stack and stack[-1] == "{":
                stack.pop()
            
            else: 
                return False
        
        if len(stack) == 0: 
            return True 
        
        return False
        
       
            
                

        