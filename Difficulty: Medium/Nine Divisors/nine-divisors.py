class Solution:
    def countNumbers(self, n):
        # Maximal potential prime factor
        limit = math.ceil(math.sqrt(n / 4)) + 1
        # Sieve of Eratosthenes
        primes = [2]
        sieve = [True] * limit
        for i in range(4, limit, 2):
            sieve[i] = False
        for i in range(3, limit, 2):
            if not sieve[i]:
                continue
            primes.append(i)
            for j in range(i * i, limit, i):
                sieve[j] = False
        # end of sieve
        count = 0
        # Case prime**8
        for p in primes:
            if p**8 > n:
                break
            count += 1
        # Case p1**2 * p2**2
        pn = len(primes)
        for p1i in range(pn):
            p1sq = primes[p1i]**2
            for p2i in range(p1i + 1, pn):
                if p1sq * primes[p2i]**2 > n:
                    break
                count += 1
        return count
        