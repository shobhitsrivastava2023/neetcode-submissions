class Solution {
    public int evalRPN(String[] tokens) {
        // reverse polish notation 

        Stack<Integer> stack = new Stack<>(); 
        for(String c : tokens){ 
            if(c.equals("+")){
                // pop previous one and previous one  
                stack.push(stack.pop() + stack.pop());
                 
            }
            else if(c.equals("-")){ 
                // pop prev and prev one 
                int a = stack.pop(); 
                int b = stack.pop(); 
                stack.push(b-a); 

            }else if(c.equals("*")){ 
                stack.push(stack.pop() * stack.pop());



            }else if(c.equals("/")){
                int a = stack.pop(); 
                int b = stack.pop(); 
                stack.push((int)((double)b/a)); 
            }
            else { 
                stack.push(Integer.parseInt(c)); 

            }
        }

        return stack.pop(); 

        
    }
}
