from collections import deque

class Solution:
    def longestSubarray(self, arr, x):
        n = len(arr)
        min_dq, max_dq = deque(), deque()
        l = 0
        best_len, best_start = 0, 0

        for r in range(n):
            while min_dq and arr[min_dq[-1]] > arr[r]:
                min_dq.pop()
            min_dq.append(r)

            while max_dq and arr[max_dq[-1]] < arr[r]:
                max_dq.pop()
            max_dq.append(r)

            while arr[max_dq[0]] - arr[min_dq[0]] > x:
                l += 1
                if min_dq[0] < l:
                    min_dq.popleft()
                if max_dq[0] < l:
                    max_dq.popleft()

            if r - l + 1 > best_len:
                best_len = r - l + 1
                best_start = l

        return arr[best_start:best_start + best_len]