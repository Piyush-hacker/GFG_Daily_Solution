class Solution:
    
    dxn=[(1,0),(-1,0),(0,1),(0,-1)]
    
    def dfs(self,mat,xd,yd,i,j):
        if i==xd and j==yd:
            return 0
        mat[i][j]=2
        ans=-1
        n,m=len(mat),len(mat[0])
        for di,dj in Solution.dxn:
            ni,nj=i+di,j+dj
            if 0<=ni<n and 0<=nj<m and mat[ni][nj]==1:
                ans=max(ans,self.dfs(mat,xd,yd,ni,nj))
        mat[i][j]=1
        return ans+1 if ans!=-1 else -1
    
    def longestPath(self, mat, xs, ys, xd, yd):
        return self.dfs(mat,xd,yd,xs,ys)