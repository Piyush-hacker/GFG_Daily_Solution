class Solution:
    def asciirange(self, s: str) -> list:
        # Step 1: Track first and last index of each character
        char_range = {}
        for i, ch in enumerate(s):
            if ch in char_range:
                char_range[ch][1] = i
            else:
                char_range[ch] = [i, i]

        # Step 2: Prefix sum of ASCII values
        prefix = [0] * (len(s) + 1)
        for i in range(len(s)):
            prefix[i+1] = prefix[i] + ord(s[i])

        # Step 3: Collect ASCII sums between first and last occurrences
        result = []
        for start, end in char_range.values():
            if end > start + 1:
                result.append(prefix[end] - prefix[start+1])

        return result