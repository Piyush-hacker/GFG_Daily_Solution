class Solution:
     def hIndex(self, citations):
        citations.sort(reverse=True)
        h = 0
        for e in citations:
            if e < h+1:
                break
            h += 1
        return h