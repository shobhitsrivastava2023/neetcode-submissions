class Solution {
public boolean hasDuplicate(int[] nums) {
    //optimal approach will include the utilization of hashmap i think 
    Set<Integer> uniques = new HashSet<>();
    for(int i = 0; i<nums.length; i++){
        if(uniques.contains(nums[i])){
            return true;
        }
        uniques.add(nums[i]);

    }
    return false;
    
    }
}
