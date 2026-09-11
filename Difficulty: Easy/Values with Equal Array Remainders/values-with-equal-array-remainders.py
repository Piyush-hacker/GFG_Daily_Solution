from math import gcd

class Solution:
    def sameMod(self, arr):
        g = 0

        # Find GCD of all differences
        for i in range(1, len(arr)):
            g = gcd(g, abs(arr[i] - arr[0]))

        # All elements are equal
        if g == 0:
            return -1

        # Count divisors of g
        count = 0
        d = 1

        while d * d <= g:
            if g % d == 0:
                count += 1

                if d != g // d:
                    count += 1

            d += 1

        return count