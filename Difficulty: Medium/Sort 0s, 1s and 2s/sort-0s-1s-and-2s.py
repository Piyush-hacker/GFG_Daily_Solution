class Solution:
    def sort012(self, arr):
        
        next0 = 0
        next2 = len(arr)-1
        curr = 0
        
        while (curr <= next2):
            
            if arr[curr] == 0:
                arr[next0], arr[curr] = arr[curr], arr[next0]
                curr+=1
                next0+=1
            elif arr[curr] == 2:
                arr[next2], arr[curr] = arr[curr], arr[next2]
                #Don't do this curr+=1 as arr[curr] can be 0 or 2 
                next2-=1
            else:
                curr+=1