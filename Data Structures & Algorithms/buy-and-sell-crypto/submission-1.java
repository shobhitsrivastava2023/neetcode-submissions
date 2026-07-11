
class Solution {
    public int maxProfit(int[] prices) {
        int maxi = 0;
        int buy = 0;
        int sell = 1;
        for(int i =0; i<prices.length-1 ; i++){
            if(prices[sell] > prices[buy]){
                maxi = Math.max(maxi, prices[sell] - prices[buy]);

            }
            else{
                buy = sell;
              
            }
              sell = sell+1;
        }
        return maxi;
    }
}
