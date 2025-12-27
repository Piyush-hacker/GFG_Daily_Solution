import numpy as np
class Solution:
     def kthSmallest(self, mat, k):
          # code here
          new = np.array(mat).ravel().tolist()
          new.sort()
          return new[k-1]