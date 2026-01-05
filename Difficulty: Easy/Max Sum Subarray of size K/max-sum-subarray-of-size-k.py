class Solution:

    def maxSubarraySum(self, arr, k):

        # Sum of first window

        window_sum = sum(arr[:k])

        max_sum = window_sum

 

        # Slide the window

        for i in range(k, len(arr)):

            window_sum += arr[i] # add next element

            window_sum -= arr[i - k] # remove element going out

            max_sum = max(max_sum, window_sum)

 

        return max_sum