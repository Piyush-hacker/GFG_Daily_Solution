class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        


class Solution:
    def sortedInsert(self, head, data):
        #code here
        first = head
        while(first.next != head):
            first = first.next
        last = first
        first = head
        
        if data <= first.data:
            node = Node(data)
            node.next = first
            last.next = node
            head = node
        elif data > last.data:
            node = Node(data)
            last.next = node
            node.next = first
            head = first
        else:
            prev = None
            while(data > first.data):
                prev = first
                first = first.next
            node = Node(data)
            prev.next = node
            node.next = first
        return head