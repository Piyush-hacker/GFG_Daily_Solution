import heapq
class Solution:
  def minOperations(self, arr):
    hp = []
    heapq.heapify(hp)
    for i in arr:
        heapq.heappush(hp,-1*i)
    s = sum(arr)
    cnt = 0
    tgt = s/2
    while s>tgt:
        a = heapq.heappop(hp)
        s+= (a/2)
        heapq.heappush(hp,a/2)
        cnt+=1
    return cnt