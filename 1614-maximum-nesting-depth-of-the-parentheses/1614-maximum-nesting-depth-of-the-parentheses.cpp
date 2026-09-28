#include <bits/stdc++.h>
class Solution {
public:
    int maxDepth(string s) {
        stack<char>st;
        int count=0;
        int max=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=='('){
                st.push(s[i]);
                count++;
                if(count>max){
                    max=count;
                }

            }
            if(s[i]==')'){
                st.pop();
                count--;
            }
        }
    return max;    
    }
};