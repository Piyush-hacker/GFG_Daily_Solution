class Solution:
    def minimumCost(self, cost, w):
        # code here
        l=[float('inf')]*(w+1)
        l[0]=0

        for i in range(len(cost)):
            if cost[i]==-1:
                continue

            wt=i+1

            for j in range(wt,w+1):
                if l[j-wt]!=float('inf'):
                    l[j]=min(l[j],cost[i]+l[j-wt])

        return -1 if l[w]==float('inf') else l[w]