'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def swapKth(self, head, k):
        curr=head
        for _ in range(k-1):
            curr=curr.next
            if curr is None:
                return head
        kth=curr
        end_kth=head
        while curr.next:
            curr=curr.next
            end_kth=end_kth.next
        kth.data,end_kth.data=end_kth.data,kth.data
        return head
        
