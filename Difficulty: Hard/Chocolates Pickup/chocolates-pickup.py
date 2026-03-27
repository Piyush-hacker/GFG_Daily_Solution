class Solution:
    def maxChocolate(self, grid):
        from functools import cache
        hth=len(grid)
        wth=len(grid[0])
        @cache
        def dp(x1=0,x2=wth-1,y=0):
            nonlocal grid,hth,wth
            if y>=hth or not(0<=x1<wth) or not(0<=x2<wth):
                return 0
            mx=-float('inf')
            for dx1,dx2 in [(0,0,),(0,1,),(0,-1,),(1,0,),(1,1,),(1,-1,),(-1,0,),(-1,1,),(-1,-1,),]:
                mx=max(mx,dp(x1+dx1,x2+dx2,y+1))
            mx+=grid[y][x1]+(grid[y][x2] if x2!=x1 else 0)
            return mx
        return dp()