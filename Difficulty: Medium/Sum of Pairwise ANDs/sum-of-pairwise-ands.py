class Solution:
    def pairAndSum(self, arr):
        # code here
        final = 0
        for i in range(32):
            count = 0
            for j in arr:
                if j & (1<<i):
                    count+=1

            new = count*(count-1)//2
            final += new*(1<<i)


        return final

