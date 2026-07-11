class Solution {
    public int[] twoSum(int[] nums, int target) {
        int achieved = 0;

        HashMap<Integer, Integer> mpp = new HashMap<>();
        for(int i = 0; i<nums.length; i++){
            int num = nums[i];
            int difference = target - num; 
            if(mpp.containsKey(difference)){
                return new int[] {mpp.get(difference), i};
            }
            mpp.put(num,i); 

        }

         return new int[] {}; 

    }
}
