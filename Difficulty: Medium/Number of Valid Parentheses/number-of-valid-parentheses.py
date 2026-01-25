class Solution:
    def findWays(self, n):
        if n==0 or n&1:
            return 0
        from functools import lru_cache
        @lru_cache(None)
        def dp(n):
            if n<=1:
                return 1
            ret=0
            for nn in range(n):
                ret+=dp(nn)*dp(n-1-nn)
            return ret
        return dp(n//2)