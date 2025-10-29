from collections import defaultdict
class Solution:
    def diameter(slf, V, edges):
        # Code here
        def f1(node):
            vis = set()
            vis.add(node)
            q = [(node, 0)]
            vv = None
            count = 0
            while(q):
                node, cnt = q.pop(0)
                vv = node
                count = cnt
                for it in adj[node]:
                    
                    if it not in vis:
                        vis.add(it)
                        q.append((it, cnt + 1))
            return vv, cnt
        
            
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        node, cnt = f1(0)
        node1, cnt = f1(node)
        return cnt
