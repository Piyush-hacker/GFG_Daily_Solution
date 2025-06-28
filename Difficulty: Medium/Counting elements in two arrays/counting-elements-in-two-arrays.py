class Solution:
    def countLessEq(self, a, b):
        maxB=max(b)
        count=[0]*(maxB+1)
        for item in b:
            count[item]+=1
        for i in range(1,maxB+1):
            count[i]+=count[i-1]
        return [count[item] if item<=maxB else count[-1] for item in a]