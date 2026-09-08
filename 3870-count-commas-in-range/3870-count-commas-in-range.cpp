class Solution {
public:
    int countCommas(int n) {
        if(n/1000>0){
            int ans=n-999;
            return ans;
        }
        else{
            return 0;
        }
    }
};