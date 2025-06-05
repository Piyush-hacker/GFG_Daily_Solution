class Solution:
    def dfs(self,adj,dest,memo,u):
        if memo[u] is None:
            if u==dest:
                return 1
            ans=0
            for v in adj[u]:
                ans+=self.dfs(adj,dest,memo,v)
            memo[u]=ans
        return memo[u]

    def countPaths(self, edges, V, src, dest):
        memo=[None]*V
        adj=[[] for _ in range(V)]
        for x,y in edges:
            adj[x].append(y)
        return self.dfs(adj,dest,memo,src)