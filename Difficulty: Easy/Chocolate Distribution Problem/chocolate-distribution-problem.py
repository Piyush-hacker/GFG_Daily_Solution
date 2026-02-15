class Solution:

    def findMinDiff(self, arr,m):
        n = len(arr)
        
        # edge cases
        if m == 0 and n == 0:
            return 0
            
        if m > n:
            return -1
            
        # Sorting the array
        arr.sort()
        
        # Initialize minimum difference
        min_diff = float('inf')
        
        # Sliding window of size m
        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            min_diff = min(min_diff, diff)
        
        return min_diff