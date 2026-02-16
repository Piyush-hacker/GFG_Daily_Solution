class Solution:
    def canAttend(self, arr):
        # sort meetings by starting timing
        arr.sort(key = lambda x : x[0])
        
        # check for overlapping meetings
        for i in range(1, len(arr)):
            # if current meeting starts before previous ends
            if arr[i][0] < arr[i-1][1]:
                return False
                
        return True