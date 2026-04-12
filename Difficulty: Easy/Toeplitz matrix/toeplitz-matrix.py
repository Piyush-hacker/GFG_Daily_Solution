class Solution:
     def isToeplitz(self, mat):
          # code here
          y, x = len(mat), len(mat[0])

          row = col = 0
          while col < x-1:
               r = row
               c = col
               while r < y-1 and c < x-1:
                    if mat[r][c] != mat[r+1][c+1]:
                         return False
                    r += 1
                    c += 1
               col += 1

          row = 1
          col = 0
          while row < y-1:
               r = row
               c = col
               while r < y-1 and c < x-1:
                    if mat[r][c] != mat[r+1][c+1]:
                         return False
                    r += 1
                    c += 1
               row += 1
          return True