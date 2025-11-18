import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, V, edges):
        adj = defaultdict(list)

        # Build adjacency list
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        src, dest = 0, V - 1

        # Dijkstra to compute shortest dist[]
        dist = [float('inf')] * V
        dist[src] = 0

        pq = [(0, src)]  # (distance, node)

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        target_dist = dist[dest]
        ans = 0

        # DFS to count number of shortest paths
        def dfs(u):
            nonlocal ans
            if u == dest:
                ans += 1
                return
            for v, w in adj[u]:
                if dist[u] + w == dist[v]:  # only follow shortest-path edges
                    dfs(v)

        dfs(src)
        return ans

