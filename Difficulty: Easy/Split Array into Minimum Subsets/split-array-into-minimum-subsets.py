class Solution:
    def minSubsets(self, arr):
        from collections import Counter
        cnt=Counter(arr)
        lst=sorted(cnt)
        lth=len(lst)
        ix=0
        ret=0
        prv=None
        while ix<lth:
            mn=lst[ix]
            cnt[mn]-=1
            if cnt[mn]==0:
                ix+=1
            if not (prv==None or prv==mn-1):
                ret+=1
            prv=mn
        return ret+1