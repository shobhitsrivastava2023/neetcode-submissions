class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] 
        def backtracking(j, temp): 
            if j == len(s): 
                res.append(temp.copy())
                return 
            tempstr = ""
            for  i in range(j, len(s)): 
                tempstr = s[j:i+1]
                if tempstr == tempstr[::-1]: 
                    temp.append(tempstr)
                    backtracking(i+1, temp)
                    temp.pop()
        backtracking(0, [])
        return res
                

                
                
                
        