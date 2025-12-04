class Solution:
    def __init__(self):
        self.dp = [[-1] * 105 for _ in range(105)]
    def recur(self, l, r, arr):
        # base cases
        if l == r:
            return arr[l][1]
        if l > r:
            return 0
        if self.dp[l][r] != -1:
            return self.dp[l][r]
        ans = float('inf')
        total_freq = 0
        for i in range(l, r + 1):
            left = self.recur(l, i - 1, arr)
            right = self.recur(i + 1, r, arr)
            ans = min(ans, left + right)
            total_freq += arr[i][1]
        self.dp[l][r] = ans + total_freq
        return self.dp[l][r]
    def minCost(self, keys, freq):
        n = len(keys)
        arr = [(keys[i], freq[i]) for i in range(n)]
        self.dp = [[-1] * 105 for _ in range(105)]
        return self.recur(0, n - 1, arr)