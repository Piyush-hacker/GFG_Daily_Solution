class Solution:
    def constructList(self, queries):
        arr = [0]
        xr = 0

        for typ, x in queries:
            if typ == 0:
                arr.append(x ^ xr)
            else:
                xr ^= x

        ans = [num ^ xr for num in arr]
        ans.sort()

        return ans