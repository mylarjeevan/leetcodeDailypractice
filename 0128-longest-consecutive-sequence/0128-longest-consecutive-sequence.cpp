// class Solution {
// public:
//     int longestConsecutive(vector<int>& nums) {
//         int n=nums.size();
//         int longest=1;
//         if(n==0){
//             return 0;
//         }
//         if(n==1){
//             return 1;
//         }
//         unordered_set<int>st;
//         for(int i=0;i<n;i++){
//             st.insert(nums[i]);
//         }
//         for(auto it:st){
//             if(st.find(it-1)==st.end()){
//                 int count=1;
//                 int x=it;
//                 while(st.find(x+1)!=st.end()){
//                     x=x+1;
//                     count++;
//                 }
//                 longest=max(longest,count);
//             }
//         }


//     return longest;

        
//     }
// };









// better solution
#include <bits/stdc++.h>
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0){
            return 0;
        }
        if(nums.size()==1){
            return 1;
        }
        sort(nums.begin(),nums.end());
        int count=1;
        int maxi=1;
        for(int i=1;i<nums.size();i++){
           if(nums[i]==nums[i-1]+1){
            count++;
            maxi=max(count,maxi);
           }
           else if(nums[i]==nums[i-1]){
            count=count;
           }
           else{
            count=1;
           }
        }
    return maxi;
        
    }
};