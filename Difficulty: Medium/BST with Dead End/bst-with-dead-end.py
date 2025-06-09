class Solution:
    def solve(self,root,minVal,maxVal):
        if not root:
            return False
        if minVal==maxVal:
            return True
        return self.solve(root.left,minVal,root.data-1) or self.solve(root.right,root.data+1,maxVal)

    def isDeadEnd(self, root):
        return self.solve(root,1,10**5)