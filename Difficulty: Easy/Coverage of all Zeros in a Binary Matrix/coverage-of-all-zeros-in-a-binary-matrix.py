class Solution:
    def findCoverage(self, mat):
        ret=0
        for rw in mat:
            zer=0
            one=False
            for x in rw:
                if x==1:
                    one=True
                    ret+=zer
                    zer=0
                else:
                    ret+=one
                    zer+=1
        for cl in zip(*mat):
            zer=0
            one=False
            for x in cl:
                if x==1:
                    one=True
                    ret+=zer
                    zer=0
                else:
                    ret+=one
                    zer+=1
        return ret