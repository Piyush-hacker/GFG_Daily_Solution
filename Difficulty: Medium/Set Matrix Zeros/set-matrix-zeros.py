class Solution:
    def setMatrixZeroes(self, mat):
        # sam
        row = len(mat)
        col = len(mat[0])
        check = [[-1 for _ in range(col)]for _ in range(row)]
        def fill(r,c):
            if check[r][c] != -1:
                return
            for i in range(row):
                if mat[i][c]!=0:
                    mat[i][c] = 0
                    check[i][c] = 0
            for i in range(col):
                if mat[r][i]!=0:
                    mat[r][i] = 0
                    check[r][i] = 0
        for i in range(row):
            for j in range(col):
                if check[i][j]==-1 and mat[i][j]==0:
                    fill(i,j)