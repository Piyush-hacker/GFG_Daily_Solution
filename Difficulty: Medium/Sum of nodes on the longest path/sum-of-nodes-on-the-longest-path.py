class Solution:
    def __init__(self):
        self.sum=0
        self.len=0
        
    def dfs(self,root,curr,l):
        curr+=root.data
        l+=1
        if self.len==l:
            self.sum=max(self.sum,curr)
        if self.len<l:
            self.len=l
            self.sum=curr
        if root.left:
            self.dfs(root.left,curr,l)
        if root.right:
            self.dfs(root.right,curr,l)
    
    def sumOfLongRootToLeafPath(self, root):
        self.dfs(root,0,0)
        return self.sum