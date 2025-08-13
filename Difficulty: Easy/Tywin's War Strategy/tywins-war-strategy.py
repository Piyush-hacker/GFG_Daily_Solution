class Solution:
    def minSoldiers(self, arr, k):
        # code here
        return (lambda target, lucky: 0 if lucky >= target else sum(sorted(k - (x % k) for x in arr if x % k)[:target - lucky]))((len(arr) + 1) // 2, sum(1 for x in arr if x % k == 0))
        