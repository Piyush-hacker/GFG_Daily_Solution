from bisect import bisect

class Solution:
    def primeList(self, head):
        def primes_upto(n):
            sieve = [1]*n
            sieve[0:2] = [0, 0]
            for i in range(2, int(n**0.5)+1):
                if sieve[i]:
                    sieve[i*i:n:i] = [0]*len(range(i*i, n, i))
            return [i for i, p in enumerate(sieve) if p]

        # Find max value in the list
        temp, max_val = head, 0
        while temp: max_val = max(max_val, temp.val); temp = temp.next

        primes = primes_upto(max_val*2)
        temp = head
        while temp:
            i = bisect(primes, temp.val)
            left, right = primes[i-1], primes[i] if i < len(primes) else float('inf')
            temp.val = left if abs(left - temp.val) <= abs(right - temp.val) else right
            temp = temp.next
        return head
        



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.val = x
        self.next = None


def printList(node):
    while (node != None):
        print(node.val, end=" ")
        node = node.next
    print()


def inputList():

    val = [int(i) for i in input().strip().split()
           ]  #all data of linked list in a line
    head = Node(val[0])
    tail = head
    for i in range(1, len(val)):
        tail.next = Node(val[i])
        tail = tail.next
    return head


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        head = inputList()

        obj = Solution()
        res = obj.primeList(head)

        printList(res)

        print("~")

# } Driver Code Ends