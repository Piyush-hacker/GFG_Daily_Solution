class Solution:

    def countAtMostK(self, arr, k):

        if k == 0:

            return 0

 

        freq = {}

        left = 0

        result = 0

 

        for right in range(len(arr)):

            freq[arr[right]] = freq.get(arr[right], 0) + 1

 

            while len(freq) > k:

                freq[arr[left]] -= 1

                if freq[arr[left]] == 0:

                    del freq[arr[left]]

                left += 1

 

            result += (right - left + 1)

 

        return result