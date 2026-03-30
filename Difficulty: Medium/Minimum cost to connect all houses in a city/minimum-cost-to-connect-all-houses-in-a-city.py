class Solution:
    def minCost(self, houses):
        ret=0
        lth=len(houses)
        import heapq
        seen=set()
        hp=[(0,0,)]
        while hp:
            cos,cur=heapq.heappop(hp)
            if cur in seen:
                continue
            ret+=cos
            seen.add(cur)
            for nxt in range(lth):
                if nxt in seen:
                    continue
                heapq.heappush(hp,(abs(houses[cur][0]-houses[nxt][0])+abs(houses[cur][1]-houses[nxt][1]),nxt,))
        return ret