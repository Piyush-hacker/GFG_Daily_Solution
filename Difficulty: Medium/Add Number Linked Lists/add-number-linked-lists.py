class Solution:
    def addTwoLists(self, head1, head2):
        # code here
        
        while head1 and head1.data == 0:
            head1 = head1.next
        
        while head2 and head2.data == 0:
            head2 = head2.next
        
        def reverse(head):
            prev = None
            curr = head
            
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            return prev
        
        head1 = reverse(head1)
        
        head2 = reverse(head2)
        res = Node(0)
        temp = res
        
        carry = 0
        
        while head1 or head2 or carry:
            s = (head1.data if head1 else 0) + (head2.data if head2 else 0) + carry
            
            carry = s // 10
            s = s%10
            
            new = Node(s)
            temp.next = new
            temp = temp.next
            
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next
        
        
        return reverse(res.next)