class Solution:
    def maxSumWithK(self, a, k):
        n = len(a)

        ans = float('-inf')
        total = 0
        last = 0
        j = 0

        for i in range(n):
            total += a[i]

            if i - j + 1 == k:
                ans = max(ans, total)

            elif i - j + 1 > k:
                last += a[j]
                j += 1

                if last < 0:
                    total -= last
                    last = 0

                ans = max(ans, total)

        return ans