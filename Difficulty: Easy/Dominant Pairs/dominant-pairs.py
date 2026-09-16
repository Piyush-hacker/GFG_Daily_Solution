class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        lth=len(arr)
        a1=sorted(arr[:lth//2])
        a2=sorted(arr[lth//2:])
        ret=0
        from bisect import bisect_left
        for n2 in a2:
            tmp=bisect_left(a1,n2*5)
            ret+=lth//2-tmp
        return ret

