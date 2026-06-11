class Solution:
     def findIndex(self, s):
          # code here
          n = len(s)
          cs = s.count(')')
          op = 0
          res = [0]*(n+1)

          for i in range(n):
               res[i] = op - cs

               if s[i] == ')':
                    cs -= 1
               if s[i] == '(':
                    op += 1
          res[-1] = op

          pos = res.index(0)
          return pos