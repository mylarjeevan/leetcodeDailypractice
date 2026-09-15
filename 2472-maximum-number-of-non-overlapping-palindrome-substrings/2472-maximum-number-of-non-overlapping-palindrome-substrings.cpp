class Solution {
public:
    int maxPalindromes(string s, int k) {
        int n = s.size();

        // pal[l][r] = whether s[l..r] is a palindrome
        vector<vector<bool>> pal(n, vector<bool>(n, false));

        for (int l = n - 1; l >= 0; --l) {
            for (int r = l; r < n; ++r) {
                if (s[l] == s[r] &&
                    (r - l <= 1 || pal[l + 1][r - 1])) {
                    pal[l][r] = true;
                }
            }
        }

        // dp[i] = answer using s[0..i-1]
        vector<int> dp(n + 1, 0);

        for (int i = 1; i <= n; ++i) {
            dp[i] = dp[i - 1];

            // Palindrome of length k ending at i-1
            if (i >= k && pal[i - k][i - 1]) {
                dp[i] = max(dp[i], dp[i - k] + 1);
            }

            // Palindrome of length k+1 ending at i-1
            if (i >= k + 1 && pal[i - k - 1][i - 1]) {
                dp[i] = max(dp[i], dp[i - k - 1] + 1);
            }
        }

        return dp[n];
    }
};