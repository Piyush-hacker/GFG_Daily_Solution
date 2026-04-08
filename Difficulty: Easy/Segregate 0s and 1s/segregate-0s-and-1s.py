class Solution:
    def segregate0and1(self, arr):
        # code here
        n = len(arr)
        l, r = 0, n-1
        while(l < r):
            while(l < r and arr[l] == 0):
                l += 1
            while(r > l and arr[r] == 1):
                r -= 1
            
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return arr

