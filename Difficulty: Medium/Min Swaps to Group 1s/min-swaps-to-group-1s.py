class Solution:
    def minSwaps(self, arr):
        window = sum(arr)
        if window == 0:
            return -1
        curr = start = 0
        ans = len(arr) + 1
        
        for i in range(len(arr)):
            curr += arr[i]
            
            if i >= window:
                curr -= arr[start]
                start += 1
            
            if i + 1 >= window:
                ans = min(ans, window - curr)
        
        return ans