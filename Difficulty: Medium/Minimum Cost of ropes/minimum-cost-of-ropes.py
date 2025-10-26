import heapq
from typing import List

class Solution:
    @staticmethod
    def minCost(arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        heapq.heapify(arr)
        res = 0

        while len(arr) >= 2:
            a = heapq.heappop(arr)
            b = heapq.heappop(arr)
            res += a + b
            heapq.heappush(arr, a + b)

        return res