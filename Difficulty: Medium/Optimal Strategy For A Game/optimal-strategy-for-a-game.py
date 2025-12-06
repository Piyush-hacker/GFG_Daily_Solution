class Solution:
    def maximumAmount(self, arr):
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        for g in range(n):  
            for i in range(n - g):
                j = i + g
                
                if i == j: 
                    dp[i][j] = arr[i]
                elif j == i + 1:  
                    dp[i][j] = max(arr[i], arr[j])
                else:
                    pick_i = arr[i] + min(dp[i+2][j] if i+2 <= j else 0,
                                          dp[i+1][j-1] if i+1 <= j-1 else 0)
                    
                    pick_j = arr[j] + min(dp[i+1][j-1] if i+1 <= j-1 else 0,
                                          dp[i][j-2] if i <= j-2 else 0)
                    
                    dp[i][j] = max(pick_i, pick_j)

        return dp[0][n-1]