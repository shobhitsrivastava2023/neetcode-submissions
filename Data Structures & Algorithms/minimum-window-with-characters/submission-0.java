class Solution {
    public String minWindow(String s, String t) {
        // two strings as input s and t
        // return shortest substring in s, which includes every char of t
        HashMap<Character, Integer> map = new HashMap<>(); 
        int matcher = 0; 
        int minimumLength = Integer.MAX_VALUE;
        int subStr =0; 
        int leftPointer = 0;
        for(int i = 0; i<t.length(); i++){
            map.put(t.charAt(i), map.getOrDefault(t.charAt(i), 0) + 1); 

        }

        for(int rightPointer = 0; rightPointer < s.length(); rightPointer++){
            char right = s.charAt(rightPointer); 
            if(map.containsKey(right)){
                map.put(right, map.get(right) -1);
                if(map.get(right) == 0){
                    matcher++; 
                }
            }
            while(matcher == map.size()){
                if(minimumLength > rightPointer - leftPointer + 1){
                    minimumLength = rightPointer - leftPointer + 1;
                    subStr = leftPointer; 
                }
                char delete = s.charAt(leftPointer++);
                if (map.containsKey(delete)) {
                
                    if (map.get(delete) == 0) {
                        matcher--;
                    }
                    map.put(delete, map.get(delete) + 1);
                }
            }
        }   
        return minimumLength > s.length() ? "" : s.substring(subStr, subStr + minimumLength); 
} 
    }
    
