class Solution:
    def countWithout(self, n: int, d: int) -> int:
        if n == 0:
            return 0
    
        s = str(n)
        ans = 0
        length = len(s)
    
        # Count numbers with fewer digits
        for digits in range(1, length):
            if d == 0:
                ans += 9 * (9 ** (digits - 1))
            else:
                ans += 8 * (9 ** (digits - 1))
    
        # Count numbers with the same number of digits
        for i in range(length):
            cur = int(s[i])
            remaining = length - i - 1
    
            if i == 0:
                smaller = cur - 1
                if d != 0 and d < cur:
                    smaller -= 1
            else:
                smaller = cur
                if d < cur:
                    smaller -= 1
    
            ans += smaller * (9 ** remaining)
    
            if cur == d:
                return ans
    
        # n itself does not contain d
        return ans + 1