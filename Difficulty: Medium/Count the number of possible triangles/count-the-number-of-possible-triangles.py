class Solution:
    def countTriangles(self, arr):
        # code here
        
        n=len(arr)
        if n<3:
            return 0
        arr.sort()
        ans=0
        for i in range(n):
            r=i-1
            l=0
            while l<r:
                if arr[l]+arr[r]>arr[i]:
                    ans+=r-l
                    r-=1
                else:
                    l+=1
        return ans