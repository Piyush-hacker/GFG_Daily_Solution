from itertools import combinations
class Solution:
    def generateIp(self, s):
        # Code here
        check = lambda word: word == '0' if word[0] == '0' else int(word) < 256
        n = len(s)
        if n > 12: return []
        ans = []
        for i, j, k in combinations(range(1,n), 3):
            if i > 3 or j - i > 3 or k - j > 3 or n - k > 3:
                continue
            tup = (s[:i], s[i:j], s[j:k], s[k:])
            if all(map(check, tup)):
                ans.append('.'.join(tup))
        return ans