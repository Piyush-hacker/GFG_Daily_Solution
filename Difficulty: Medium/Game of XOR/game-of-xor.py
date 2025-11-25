class Solution:
    def subarrayXor(self, arr):
        n=len(arr)
        ans=0
        for i in range(n):
            if ((i+1)*(n-i))&1:
                ans^=arr[i]
        return ans
        