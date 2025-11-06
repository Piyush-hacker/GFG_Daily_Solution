class Solution:
    def numberOfWays(self, n):
        if n<3:
            return n
        x=1
        y=2
        for i in range(2,n):
            x,y=y,x+y
        return y