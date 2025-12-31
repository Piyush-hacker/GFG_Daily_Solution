class Solution:
    def isPalindrome(self, head):
        # code here
        s=[]
        while head:
            s.append(str(head.data))
            head = head.next
        return all(s[i] == s[len(s) - i - 1] for i in range(len(s) // 2))