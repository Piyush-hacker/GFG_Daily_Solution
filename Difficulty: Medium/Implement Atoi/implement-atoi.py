class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        res = 0
        i = 0
        n = len(s)
        
        # Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Check for sign
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Convert numeric characters
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            
            # Overflow check before updating res
            if res > (2**31 - 1) // 10 or (res == (2**31 - 1) // 10 and digit > 7):
                return (2**31 - 1) if sign == 1 else -2**31
            
            res = res * 10 + digit
            i += 1

        return res * sign