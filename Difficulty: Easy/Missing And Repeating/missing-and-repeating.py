from collections import Counter
class Solution:
    def findTwoElement(self, arr):
        d=Counter(arr)
        res=[0,0]
        l=len(arr)
        for i in range(1,l+1):
            if i in d and d[i]==2:
                res[0]=i
            elif i not in d:
                res[1]=i
        return res