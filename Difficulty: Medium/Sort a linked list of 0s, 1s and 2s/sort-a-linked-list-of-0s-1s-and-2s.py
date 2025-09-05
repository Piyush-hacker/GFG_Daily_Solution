'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        zero,one,two=Node(-1),Node(-1),Node(-1)
        zh,oh,th=zero,one,two
        curr=head
        while curr:
            if curr.data==0:
                zero.next=curr
                zero=zero.next
            elif curr.data==1:
                one.next=curr
                one=one.next
            else:
                two.next=curr
                two=two.next
            curr=curr.next
        zero.next,one.next,two.next=None,None,None
        head=Node(-1)
        tail=head
        if zh.next:
            tail.next=zh.next
            tail=zero
        if oh.next:
            tail.next=oh.next
            tail=one
        if th.next:
            tail.next=th.next
            tail=two
        return head.next
    