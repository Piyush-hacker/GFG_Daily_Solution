class Solution:
    def distinctSubseq(self, s):
        MOD = 10**9 + 7
        
        # total number of distinct subsequences so far
        # start with 1 for the empty subsequence ""
        total = 1
        
        # last_contrib[ch_index] will store the number of subsequences
        # counted BEFORE the previous occurrence of that character
        last_contrib = [0] * 26  # for 'a' to 'z'
        
        for ch in s:
            idx = ord(ch) - ord('a')
            
            # New total is double the previous total (either include or exclude ch)
            # minus the subsequences that would be duplicated due to previous same character
            new_total = (2 * total - last_contrib[idx]) % MOD
            
            # Update last contribution for this character
            last_contrib[idx] = total
            
            # Move to new total
            total = new_total
        
        # total already counts all distinct subsequences (including the empty one)
        return total % MOD
