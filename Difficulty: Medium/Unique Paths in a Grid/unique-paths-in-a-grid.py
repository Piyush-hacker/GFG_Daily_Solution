class Solution:
    def uniquePaths(self, grid):
        n,m=len(grid),len(grid[0])
        dp=[[None]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    if i==0 and j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=(dp[i-1][j] if i-1>=0 else 0)
                        dp[i][j]+=(dp[i][j-1] if j-1>=0 else 0)
                else:
                    dp[i][j]=0
        return dp[n-1][m-1]