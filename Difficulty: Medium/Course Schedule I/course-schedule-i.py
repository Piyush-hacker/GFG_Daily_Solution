class Solution:
    def canFinish(self, n, pre):
        temp = [-1]*n
        for i in pre:
            temp[i[0]]=i[1]
        for i in temp:
            if i==-1:
                return True
        return False