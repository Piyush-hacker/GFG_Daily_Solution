class Solution:
	 def mergeOverlap(self, arr):
        # Code here
        arr.sort()
        ans = []
        running = arr[0]
        for i in range(1, len(arr)):
            if running[1] < arr[i][0]:
                ans.append(running)
                running = arr[i]
            else:
                running = (min(running[0], arr[i][0]), max(running[1], arr[i][1]))
              
        return ans + [running]