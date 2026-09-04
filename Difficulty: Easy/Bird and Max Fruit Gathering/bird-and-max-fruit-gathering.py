class Solution:
    def maxFruits(self, arr: list[int], m: int) -> int:
        lth=len(arr)
        mx=sm=0
        for ix in range(lth+m):
            sm+=arr[ix%lth]-(arr[ix-m] if ix-m>=0 else 0)
            mx=max(mx,sm)
        return mx