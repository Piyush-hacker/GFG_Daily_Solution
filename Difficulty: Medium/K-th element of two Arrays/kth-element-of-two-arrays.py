class Solution:
    def kthElement(self, a, b, k):
        # code here
        li = []
        li = a + b
        li.sort()
        return li[k-1]