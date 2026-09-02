class Solution:
    def solve(self, n, s):
       using = set()
       rejected = set()
    
       for ch in s:
           if ch in using:
               # Customer leaves
               using.remove(ch)
    
           elif ch in rejected:
               # Rejected customer's departure - do nothing
               pass
    
           else:
               # Customer arrives
               if len(using) < n:
                   using.add(ch)
               else:
                   rejected.add(ch)
    
       return len(rejected)