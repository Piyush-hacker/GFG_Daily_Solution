import math
class Solution:
    def hours_needed(self,arr,x):
        ans=0
        for item in arr:
            ans+=math.ceil(item/x)
        return ans
    
    def kokoEat(self,arr,k):
        l,h=1,max(arr)
        while l<=h:
            mid=(l+h)//2
            if self.hours_needed(arr,mid)>k:
                l=mid+1
            else:
                h=mid-1
        return l