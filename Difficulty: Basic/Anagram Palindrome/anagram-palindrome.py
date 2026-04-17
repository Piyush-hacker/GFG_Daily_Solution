from collections import Counter
class Solution:
     def canFormPalindrome(self, s):
          # code here
          st = Counter(s)
          return sum(x & 1 for x in st.values()) <= 1