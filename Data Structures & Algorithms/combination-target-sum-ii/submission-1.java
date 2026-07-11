class Solution {
    public List<List<Integer>> combinationSum2(int[] arr, int target) {
        List<List<Integer>> list=new ArrayList<>();
        List<Integer> temp=new ArrayList<>();
        Arrays.sort(arr);
        int n=arr.length;
        solver(0,arr,list,temp,target,n);
        return list;
    }
    private void solver(int ind,int []arr,List<List<Integer>> list,List<Integer> temp,int target,int n){
        if(target==0){
            if(list.contains(temp)){
                return;
            }
            list.add(new ArrayList<>(temp));
            return;
        }
        if(ind>=n){
            return ;
        }
        if(target>=arr[ind]){
            temp.add(arr[ind]);
            solver(ind+1,arr,list,temp,target-arr[ind],n);
            temp.remove(temp.size()-1);
        }
        solver(ind+1,arr,list,temp,target,n);
    }
}
