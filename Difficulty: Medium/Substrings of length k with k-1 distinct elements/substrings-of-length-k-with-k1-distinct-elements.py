class Solution:
    def substrCount(self, s, k):
        d = dict()
        start = ans = 0
        
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
            
            if i + 1 >= k:
                while len(d) > k - 1 or i - start + 1 > k:
                    d[s[start]] -= 1
                    
                    if d[s[start]] == 0:
                        del d[s[start]]
                    
                    start += 1
                    
                if i - start + 1 == k and len(d) == k - 1:
                    ans += 1
                        
        return ans