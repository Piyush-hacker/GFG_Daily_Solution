'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def isSymmetric(self, root):
        #Code Here
        
        def check(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 and n2 or n1 and not n2 or n1.data != n2.data:
                return False
            
            return check(n1.left, n2.right) and check(n1.right, n2.left)
        
        if not root:
            return True
        return check(root.left, root.right)