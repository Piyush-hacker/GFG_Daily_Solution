class Solution:
   def minCost(self, height):
        n=len(height)
        if n==1:
            return 0
        a,b=0,abs(height[0]-height[1])
        for i in range(3,n+1):
            b,a=min(b+abs(height[i-1]-height[i-2]),a+abs(height[i-1]-height[i-3])),b
        return b