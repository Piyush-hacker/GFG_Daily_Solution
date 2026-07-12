class Solution:
    def maxAmount(self, arr, k):
        import heapq
        hp=[-ve for ve in arr]
        heapq.heapify(hp)
        ret=0
        for _ in range(k):
            if hp:
                ve=-heapq.heappop(hp)
                ret+=ve
                ret%=1_000_000_007
                if ve>=2:
                    ve-=1
                    heapq.heappush(hp,-ve)
                continue
            break
        return ret