class Solution:
    def getMaxSum(self, root):
        def dfs(cur=root):
            if not cur:
                return 0,0
            li,le=dfs(cur.left)
            ri,re=dfs(cur.right)
            return cur.data+le+re,max(li+ri,li+re,le+ri,le+re)
        return max(dfs())