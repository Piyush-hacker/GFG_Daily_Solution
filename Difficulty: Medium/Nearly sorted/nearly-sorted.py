import heapq
class Solution:
    def nearlySorted(self, arr, k):  
        tmp = []
        i = 0
        for num in arr:
            heapq.heappush(tmp, num)
            if len(tmp) > k:
                arr[i] = heapq.heappop(tmp)
                i+=1
        
        while tmp:
            arr[i] = heapq.heappop(tmp)
            i+=1
            