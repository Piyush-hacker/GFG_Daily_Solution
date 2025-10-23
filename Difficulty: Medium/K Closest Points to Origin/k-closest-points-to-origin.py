import heapq
class Solution:
    def kClosest(self, points, k):
        # code here
        diffs = []
        for p in points:
            heapq.heappush(diffs, (p[0]**2 + p[1]**2, p))
        
        return [p[1] for p in heapq.nsmallest(k, diffs)]