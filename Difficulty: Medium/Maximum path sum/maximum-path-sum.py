'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxSum(self, root):
        def dfs(cur=root):
            if not cur:
                return -float('inf'),-float('inf')
            l,l2=dfs(cur.left)
            r,r2=dfs(cur.right)
            c=max(l,r)+cur.data
            c=max(c,cur.data)
            c2=max(l2,r2,l+cur.data+r,l,r,l+cur.data,r+cur.data)
            return c,c2
        return max(dfs())