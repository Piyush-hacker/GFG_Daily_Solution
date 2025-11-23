class Solution:
        def minConnect(self, V, edges):
            E = len(edges)
            if E < V - 1:
                return -1
            parent = list(range(V))
            rank = [0] * V
            
            def find(u: int) -> int:
                if u != parent[u]:
                    parent[u] = find(parent[u])
                return parent[u]
            
            def union(u: int, v: int) -> bool:
                u, v = find(u), find(v)
                if u == v:
                    return False
                if rank[u] >= rank[v]:
                    parent[v] = u
                else:
                    parent[u] = v
                if rank[u] == rank[v]:
                    rank[u] += 1
                return True
            
            for u, v in edges:
                union(u, v)
            return len(set(map(find, range(V)))) - 1
        
