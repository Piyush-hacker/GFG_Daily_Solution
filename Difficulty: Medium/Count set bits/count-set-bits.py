class Solution:
    def countSetBits(self, n):
        k = n.bit_length()
        dp = {1: 1, 0: 0}
        # Precomputing the "full sub-problems"
        for bits in range(2, 31):
            mask = (1 << bits) - 1
            dp[mask] = 2 * dp[mask >> 1] + (1 << bits - 1)
        
        def A(n):
            if n not in dp:
                msb = 1 << n.bit_length() - 1
                lower_part = msb - 1
                dp[n] = (
                    # Full sub-problem, the msb == 0
                    A(lower_part)
                    # How many times do we see the msb == 1
                    + n - lower_part
                    # Partial sub-problem, for n without msb
                    + A(n ^ msb)
                )
            return dp[n]
        return A(n)